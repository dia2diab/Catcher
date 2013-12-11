#! /usr/bin/env python

from sys import argv
from core.forhelp import forhelp
from core.sqlconnection import Connection
from core.extractor import Extractor
from core.compare import Compare


def main():
    if len(argv) <= 1:
        forhelp()
        exit(1)

    else:
        if len(argv) == 2:
            if argv[1] in ['-c', '--clear']:
                Connection().drop()
                Extractor().cls()

            elif argv[1] in ['-p', '--compare']:
                com = Compare().result()
            else:
                forhelp()
                exit(1)

        elif len(argv) == 4:
            target = argv[3]

            if argv[1] in ['-f', '--first-shot'] and \
                    argv[2] in ['-t', '--target']:
                    ex = Extractor(target, 1)
                    ex.walk()

            elif argv[1] in ['-s', '--second-shot'] and \
                    argv[2] in ['-t', '--target']:
                        ex = Extractor(target, 2)
                        ex.walk()

            else:
                forhelp()
                exit(1)

        else:
            forhelp()
            exit(1)

if __name__ == '__main__':
    main()
