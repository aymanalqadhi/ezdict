#!/usr/bin/env python3

import itertools
import math

from ezdict.tokens.token_combiner_base import TokenCombinerBase
from ezdict.tokens.name_token import NameToken

def product(nums: list) -> int:
    ret = 1
    for n in nums:
        ret *= n
    return ret

class BruteforceTokenCombiner(TokenCombinerBase):
    """ A Class to get all possible combinations of a set of tokens """
    def __init__(self, tokens: list, allow_empty=True):
        self.tokens = tokens
        self.allow_empty = allow_empty

    def combine(self, on_tokens_combined: callable) -> bool:
        """ Base class method override """
        values = []
        for token in self.tokens:
            values.append(list(dict.fromkeys(token.get_possible_words())))

        items_count = product([len(v) for v in values])\
                      * math.factorial(len(self.tokens)) + 2

        for i in range(1, len(values) + 1):
            for sub in itertools.combinations(values, i):
                for comb in itertools.product(*sub):
                    for item in itertools.permutations(comb, len(comb)):
                        on_tokens_combined(''.join(item), 0.0)

        return True
