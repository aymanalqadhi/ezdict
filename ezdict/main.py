#!/usr/bin/env python3

import sys

from ezdict.config import args_parser

from ezdict.commands.person_dict import PersonDict

if __name__ == '__main__':
    # Parse main command line options
    if len(sys.argv) <= 1:
        args_parser.parse_args()
        sys.exit(1)

    app_args = args_parser.parse_args([sys.argv[1]])
    cmd_args = sys.argv[2:]

    # Get all app commands
    app_commands = [ PersonDict(cmd_args) ]

    # Get the choosen command
    command = [ cmd for cmd in app_commands if cmd.name == app_args.command ]
    if len(command) <= 0:
        raise NameError('No such command: %s' % app_args.command)

    # Parse the command args and then execute it
    command[0].configure()
    command[0].execute()
