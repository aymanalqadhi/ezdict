import argparse

# App info constants
APP_NAME         = 'ezdict'
APP_VERSION      = '0.1'
APP_DESC         = 'A tool for generating passwords word lists'
APP_AUTHOR_NAME  = 'Ayman Al-Qadhi'
APP_AUTHOR_EMAIL = 'alqadh1@outlook.com'

# Create Main arguments parser
args_parser = argparse.ArgumentParser(description=APP_DESC)

# Add main arguments
args_parser.add_argument(dest='command',
                  help='Command to execute',
                  choices=[ 'person_dict', 'bruteforce_dict' ])
