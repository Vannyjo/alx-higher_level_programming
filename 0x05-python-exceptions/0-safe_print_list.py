#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elmnt_list = 0
    for a in range(x):
        try:
            print(f"{my_list[i]}", end="")
            elmnt_list += 1
        except IndexError:
            break
    print()
    return elmnt_list
