#!/usr/bin/env python3
"""Personal data"""

import re


def filter_datum(fields, redaction, message, separator):
    """Define filter datum"""
    regex = '|'.join(f'({field}=.*?)({separator}|$)' for field in fields)
    return re.sub(regex, rf'\1{redaction}\2', message)
