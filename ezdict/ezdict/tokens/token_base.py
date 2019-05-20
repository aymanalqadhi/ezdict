#!/usr/bin/env python3

class TokenBase():
    """ Base class of all tokens """
    def get_possible_words(self) -> list:
        """ Gets all possible words that can be made out of this token """
        raise NotImplemented
