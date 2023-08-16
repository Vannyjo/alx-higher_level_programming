#!/usr/bin/python3
import sys

def infinite_add():
    # Sum up all the arguments after converting them to integers
    result = sum(int(arg) for arg in sys.argv[1:])
    print(result)

# Ensure the code isn't executed when the module is imported
if __name__ == "__main__":
    infinite_add()

