#!/usr/bin/env python3

from ezdict.commands.command_base import CommandBase
from ezdict.utils.input import *

from ezdict.tokens.name_token import NameToken
from ezdict.tokens.number_token import NumberToken
from ezdict.tokens.date_token import DateToken

from ezdict.tokens.bruteforce_token_combiner import BruteforceTokenCombiner

import sys
import os
import argparse

# Command info
COMMAND_NAME        = 'person_dict'
COMMAND_DISCRIPTION = 'A Command to generate a dictionary out of a person info'

class PersonDict(CommandBase):
    """
    A Command to generate a dictionary out of a person information such
    as his name, DOB, pet's name, favorate sport, etc...
    """
    def __init__(self, args_list: list) -> None:
        # Call base constructor with command info
        CommandBase.__init__(
                self,
                name        = COMMAND_NAME,
                description = COMMAND_DISCRIPTION,
                args_list   = args_list)

    def execute(self) -> None:
        """ Base class method override """
        tokens = []

        # Add names tokens
        if self.args.names:
            for t in load_names(self.args.names):
                if len([tok.name for tok in tokens if tok.name == t]) == 0:
                    tokens.append(NameToken(
                        t,
                        use_common_symboles = self.args.use_common_symboles,
                        switch_cases        = self.args.use_switched_case_names,
                        reverse             = self.args.use_reversed_names))

        # Add numbers tokens
        if self.args.numbers:
            for t in load_phones(self.args.numbers):
                tokens.append(NumberToken(
                    t,
                    reverse  = self.args.flip_numbers,
                    portions = self.args.sub_numbers))

        # Add dates tokens
        if self.args.dates:
            for t in load_dates(self.args.dates):
                tokens.append(DateToken(t))

        bruteforce_combiner = BruteforceTokenCombiner(tokens)
        bruteforce_combiner.combine(
                lambda w, p: self.args.outfile.write(w + '\n'))

    def configure(self) -> None:
        """ Base class method override """
        # Add arguments
        # Names arguemnts
        self.args_parser.add_argument('-n', '--names',
                dest    = 'names',
                help    = 'A file containing names to use',
                type    = argparse.FileType('r'),
                default = None)
        self.args_parser.add_argument('-r', '--reversed-names',
                dest    = 'use_reversed_names',
                action  = 'store_true',
                help    = 'Reverse entered names',
                default = False)
        self.args_parser.add_argument('-s', '--switched-case-names',
                dest    = 'use_switched_case_names',
                action  = 'store_true',
                help    = 'Siwtch the case of the names characters',
                default = False)
        self.args_parser.add_argument('-c', '--common-symboles',
                dest    = 'use_common_symboles',
                action  = 'store_true',
                default = False)

        # Numbers arguments
        self.args_parser.add_argument('-p', '--numbers',
                dest    = 'numbers',
                help    = 'A file containing phone numbers to use',
                type    = argparse.FileType('r'),
                default = None)
        self.args_parser.add_argument('-b', '--sub-numbers',
                dest    = 'sub_numbers',
                action  = 'store_true',
                help    = 'Use portions of the used numbers',
                default = False)
        self.args_parser.add_argument('-f', '--flip-numbers',
                dest    = 'flip_numbers',
                action  = 'store_true',
                help    = 'Flips the numbers',
                default = False)

        # Other arguments
        self.args_parser.add_argument('-d', '--dates',
                dest    = 'dates',
                help    = 'A file containing dates to use',
                type    = argparse.FileType('r'),
                default = None)
        self.args_parser.add_argument('-o', '--output',
                dest    = 'outfile',
                help    = 'The output file ( \'-\' for fd 3 )',
                type    = argparse.FileType('w'),
                default = '-')

        # Call the base method to parse the arguments
        CommandBase.configure(self)
