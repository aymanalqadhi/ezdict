#!/usr/bin/env python3

import sys
import argparse

class CommandBase():
    """
    A Class to represent a command executed with command line arguments list
    """ 
    def __init__(self, name: str, description: str, args_list: list):
        # Set command information
        self.name        = name
        self.description = description
        self.args_list   = args_list

        # Create an arguments parser
        self.args_parser = argparse.ArgumentParser(
                prog        = "%s %s" % (sys.argv[0], self.name),
                description = self.description)

    def configure(self) -> None:
        """ Parses and validates the passed command line arguments """
        self.args = self.args_parser.parse_args(self.args_list)

    def execute(self) -> None:
        """ Executes the command """
        raise NotImplementedError
