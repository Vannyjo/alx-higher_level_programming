#!/usr/bin/python3
def simple_delete(my_dic, key=""):
    if key in my_dic:
        del my_dic[key]
    return my_dic
