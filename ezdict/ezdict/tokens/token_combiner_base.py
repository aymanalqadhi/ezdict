#!/usr/bin/env python3

from ezdict.tokens.token_base import TokenBase

class TokenCombinerBase():
    """ The base class of all token combiners """
    def __init__(self, tokens: list):
        self.tokens = tokens

    def combine(self, on_tokens_combined: callable) -> bool:
        """ Generates all possible combinations of supplied tokens """
        raise NotImplemented
