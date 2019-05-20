#!/usr/bin/env python3

from ezdict.tokens.token_base import TokenBase

import datetime

class DateToken(TokenBase):
    """ A token to handle dates """
    def __init__(self, date: datetime.date):
        self.date = date

    def get_possible_words(self):
        """ Base class method override """
        ret = [ self.date.year, self.date.year % 100 ]
        return [ str(d) for d in ret ]
