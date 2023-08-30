#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    tred = 0
    for j in range(x):
        try:
            print(f"{my_list[j]}", end="")
            tred += 1
        except IndexError:
            break
    print()
    return(tred)
