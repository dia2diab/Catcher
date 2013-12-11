#! /usr/bin/env python

import os
import sys


class Output(object):

    def __init__(self, kind):
        self.__myPath = None
        self.__outdir = 'shots'
        if kind == 1:
            self.__outfile = 'FirstShot.txt'
        else:
            self.__outfile = 'SecondShot.txt'
        self.o_file = None

    def now_dir(self):
        self.__myPath = os.getcwd()

    def out_dir(self):
        outdir = os.path.join(self.__myPath,
                self.__outdir)
        if self.__myPath:
            print '[-] creating dir for output...'
            if not os.path.exists(outdir):
                try:
                    os.mkdir(outdir)
                    print '[+] successfully dir created.. [Done]'
                    print '[+] path : {0}'.format(outdir)

                except OSError:
                    print '[!] can\'t create dir for output.'
                    raise(OSError, 'you do not have permission here.')
            else:
                print '[+] output dir is already exist.. [Done]'
                print '[+] path : {0}'.format(outdir)

    def out_file(self):
        outfile = os.path.join(self.__myPath,
                self.__outdir, self.__outfile)
        if self.__myPath:
            if not os.path.exists(outfile):
                if self.__outfile == 'SecondShot.txt':
                    first = os.path.join(self.__myPath,
                    self.__outdir, 'FirstShot.txt')
                    if not os.path.exists(first):
                        print '[!] you must take first shot from the target !!'
                        exit(0)

                try:
                    print '[-] creating file for output...'
                    try:
                        self.o_file = open(outfile, 'w')
                    except IOError:
                        raise(IOError, 'I/O error.')
                    if self.o_file:
                        print '[+] successfully file created.. [Done]'
                        print '[+] path : {0}'.format(outfile)
                        print

                except OSError:
                    print '[!] can\'t create file for out.'
                    raise(OSError, 'you do not have permission here.')
            else:
                print '[!] run < ./catcher.py -c > to clear previous shots !!'
                exit(0)
                try:
                    self.o_file = open(outfile, 'a')
                    btween = '===' * 20 + '\n'
                    self.write(btween)
                except IOError:
                    raise(IOError, 'I/O error.')

    def write(self, txt):
        self.o_file.writelines(txt)

    def close(self):
        self.o_file.close()

    def nowpath(self):
        return self.__myPath
