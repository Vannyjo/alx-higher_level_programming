#!/usr/bin/python3
def best_score(d_dic):
    if d_dic and len(d_dic):
        max = list(d_dic.keys())[0]
        for key in d_dic:
            if d_dic[key] > d_dic[max]:
                max = key
        return max
    return None
