#!/usr/bin/python3

def no_c(my_string):
    updated_str = ''
    for k in my_string:
        if k != 'c' and k != 'C':
            updated_str += k
    return (updated_str)
