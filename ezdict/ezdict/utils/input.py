#!/usr/bin/env python3

import datetime

def is_valid_int(value: str):
    """ Checks whether the input is an integeral value or not """
    try:
        int(value)
        return True
    except:
        return False

def is_valid_date(value: str):
    """ Checks whether the input is a date value or not """
    fields = value.split('/')
    return len(fields) == 3 and is_valid_int(fields[0]) and \
           is_valid_int(fields[1]) and is_valid_int(fields[2]) 

def load_dates(infile) -> list:
    """ Loads a list of dates from a file """
    for date in infile.readlines():
        try:
            f = date.split('/')
            ret = datetime.date( int(f[0]), int(f[1]), int(f[2]))
            yield ret
        except:
            break

def load_names(infile) -> list:
    """ Loads a list of names from a file """
    for name in infile.readlines():
        yield name.rstrip('\n')

def load_phones(infile) -> list:
    """ Loads a list of phone numbers from a file """
    for phone in infile.readlines():
        yield phone.rstrip('\n')
