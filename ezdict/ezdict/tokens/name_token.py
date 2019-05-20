#!/usr/bin/env python3

from ezdict.tokens.token_base import TokenBase

class NameToken(TokenBase):
    """ A token for names values """
    def __init__(
            self, name: str,
            switch_cases        = True,
            reverse             = True,
            use_common_symboles = False):
        self.name                = name
        self.use_switched_cases  = switch_cases
        self.use_reversed        = reverse
        self.use_common_symboles = use_common_symboles

    def get_possible_words(self):
        """ Base class method override """
        words = [ self.name ]

        # Add switched-case values
        if self.use_switched_cases:
            words.extend(self.get_switched_cases())
        # Add revesed words
        if self.use_reversed:
            rev = []
            for word in words:
                to_add = word[::-1]
                if to_add not in rev and to_add not in words:
                    rev.append(to_add)
            words.extend(rev)

        return words

    def get_switched_cases(self) -> list:
        """ Gets all case combinations of a name """
        ret = []
        copy = self.name
        for n in range(2 ** len(copy)):
            for i in range(len(copy)):
                if n & (1 << i) == 0:
                    copy = copy[0:i] + copy[i].lower() + copy[i + 1:]
                else:
                    copy = copy[0:i] + copy[i].upper() + copy[i + 1:]
            if not copy in ret:
                ret.append(copy)
        return ret
