#!/usr/bin/env python3

import itertools

from ezdict.tokens.token_base import TokenBase

def get_all_substrings(string: str) -> list:
    length = len(string)
    items = [string[i:j+1] for i in range(length) for j in range(i, length)]
    ret = []
    for item in items:
        if not item in ret:
            ret.append(item)
    return ret

class NumberToken(TokenBase):
    """ A token for numeric values """
    def __init__(
            self,
            number: int,
            reverse: bool  = True,
            portions: bool = False):
        self.number       = number
        self.use_reversed = reverse
        self.use_portions = portions

    def get_possible_words(self) -> list:
        """ Base class method overrdie """
        num_str = str(self.number)
        ret = []

        # Add portions
        if self.use_portions:
            ret.extend(get_all_substrings(num_str))
        else:
            ret.append(num_str)

        # Add reverse
        if self.use_reversed:
            rev = []
            for n in ret:
                rev.append(n[::-1])
            ret.extend(rev)

        return ret
