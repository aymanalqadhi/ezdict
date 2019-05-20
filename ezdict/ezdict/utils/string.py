#!/usr/bin/env python3

def reverse_str(name: str) -> str:
    """ Reverses a string """
    name_lst = list(name)
    name_lst.reverse()
    ret = ''
    for i in range(len(name_lst)):
        ret += name_lst[i]
    return ret
