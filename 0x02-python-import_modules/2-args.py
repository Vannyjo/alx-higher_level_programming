#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("Number of argument(s): 0.")
        print(".")
    else:
        if argc == 1:
            print("Number of argument(s): 1: {}.".format(argv[1]))
            print("1: {}.".format(argv[1]))
        else:
            print("Number of argument(s): {}: {}.".format(argc, ' '.join(argv[1:])))
            for i, arg in enumerate(argv[1:], start=1):
                print("{}: {}.".format(i, arg))

