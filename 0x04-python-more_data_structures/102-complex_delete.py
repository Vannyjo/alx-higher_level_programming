#!/usr/bin/python3
def complex_delete(python_dict, value):
    keys_to_del = []
    for key in python_dict:
        if python_dict[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del python_dict[key]
    return python_dict
