#! /usr/bin/env python

import os
import copy
from sqlconnection import Connection

class Compare(object):
    def __init__(self):
        self.target = None
        self.firstShot = None
        self.secondShot = None
        self.nothing = None
        self.delete = []
        self.edit = []
        self.add = []
        self.rename = []

    def sure(self):
        now = os.getcwd()
        checked = now + '/shots'
        done = 0
        for f in ['FirstShot.txt', 'SecondShot.txt']:
            if os.path.exists(os.path.join(checked, f)):
                done +=1

        if done == 0:
            print '[!] you must take two shots to be compared !!'
            print '[!] run < ./catcher.py -h > for help.'
            exit(0)

        elif done == 1:
            print '[!] you must take the second shot !!'
            print '[!] run < ./catcher.py -h > for help.'

        if done == 2:
            target1 = open(os.path.join(checked, 'FirstShot.txt')).readline()
            target1 = target1.splitlines()[0].split(' ')[2]

            target2 = open(os.path.join(checked, 'SecondShot.txt')).readline()
            target2 = target2.splitlines()[0].split(' ')[2]

            if target1 != target2:
                print '[!] target in first shot differ from target in second shot !!'
                print '[!] run < ./catcher.py -h> for help.'
                exit(0)

            else:
                self.target = target1

    def getData(self):
        db = Connection()
        self.firstShot = db.getAll(1)
        self.secondShot = db.getAll(2)

    def compare(self):
        print '[-] comparing two shots ...'
        if self.firstShot == self.secondShot:
            self.nothing = 1
            return

        for element in self.firstShot:
            for ele in self.secondShot:
                if element == ele:
                    index = self.secondShot.index(ele)
                    self.secondShot.remove(self.secondShot[index])

        tmp = copy.copy(self.secondShot)
        for remain in self.secondShot:
            name = remain[0]
            md5 = remain[2]
            for m in self.firstShot:
                if name == m[0] and md5 != m[2]:
                    self.edit.append(remain)
                    index = tmp.index(remain)
                    tmp.remove(tmp[index])
                    break

                elif name != m[0] and md5 == m[2]:
                    self.rename.append(remain)
                    index = tmp.index(remain)
                    tmp.remove(tmp[index])
                    break

        self.add = tmp
        print '[+] comparing two shots.. [Done]'

    def result(self):
        self.sure()
        self.getData()
        self.compare()
        self.resbanner()

        print 'Result: '
        print '-------'
        if self.nothing == 1:
            print "[+] no changes in the target path. (great)"
        else:
            if self.add:
                print "Added Files: "
                for a in self.add:
                    print "name: " + str(a[0])
                    print "path: " + str(a[1])
                    print "md5: " + str(a[2])
                    print
                print

            if self.rename:
                print "Renamed Files: "
                for r in self.rename:
                    print "name: " + str(r[0])
                    print "path: " + str(r[1])
                    print "md5: " + str(r[2])
                    print
                print

            if self.edit:
                print "Edited Files: "
                for e in self.edit:
                    print "name: " + str(e[0])
                    print "path: " + str(e[1])
                    print "md5: " + str(e[2])
                    print
                print

    def resbanner(self):
        print '''
*********************************************
             | |        | |
  ___   __ _ | |_   ___ | |__    ___  _ __
 / __| / _` || __| / __|| '_ \  / _ \| '__|
| (__ | (_| || |_ | (__ | | | ||  __/| |
 \___| \__,_| \__| \___||_| |_| \___||_|
*********************************************
        '''
