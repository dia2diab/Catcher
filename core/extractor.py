#! /usr/bin/env python

import os
import hashlib
from output import Output
from sqlconnection import Connection


class Extractor(object):

    def __init__(self, path="", kind=None):
        if os.path.exists(path) and os.path.isabs(path):
            self.__path = path
        else:
            self.__path = os.getcwd()
        self.kind = kind
        self.md5list = []
        self.co = Connection()

    def walk(self):
        self.co.create()
        output = Output(self.kind)
        output.now_dir()
        print '[+] now path: ' + str(output.nowpath())
        output.out_dir()
        output.out_file()
        print '[+] target path: ' + str(self.__path)
        header = "target : " + self.__path + '\n'
        print '[+] please wait ...'
        output.write(header)
        for root, dirs, files in os.walk(self.__path):
            level = root.replace(self.__path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            out = '{0}--=> {1}/'.format(indent, os.path.basename(root)) + '\n'
            output.write(out)
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                #c_path = os.path.basename(root) + '/' + f
                f_name = f
                f_path = os.path.join(root, f)
                if self.checking(f_path) == 2:
                    f_md5 = self.md5(f_path)
                    self.co.into(self.kind, f_name, f_path, f_md5)
                out = '{0}=> {1}'.format(subindent, f) + '\n'
                output.write(out)
        self.co.close()
        output.close()

    def md5(self, path, hex=True, hash_type=hashlib.md5):
        hashinst = hash_type()
        try:
            with open(path, 'rb') as f:
                for chunk in iter(lambda: f.read(hashinst.block_size * 128), b''):
                    hashinst.update(chunk)
            return hashinst.hexdigest() if hex else hashinst.digest()
        except:
            print '[!] error [Permission denied] !!'
            exit(0)

    def cls(self):
        files = ['FirstShot.txt', 'SecondShot.txt']
        for f in files:
            fname = self.__path + "/shots/" + f
            if os.path.isfile(fname):
                os.remove(fname)
        print '[+] deleting shots files .. [Done]'

    def checking(self, path):
        if os.path.isdir(path):
            return 1
        elif os.path.isfile(path):
            return 2
        else:
            return 3
