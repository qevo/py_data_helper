"""Check for a condition"""

import re


def is_str(x):
    """Returns True is x is a string, otherwise False is returned

    Args:
        x (string): Any string

    Returns:
        bool: True if x is a string, otherwise False is returned

    """
    return type(x) == str


def is_int(x):
    """Returns True is x is an integer, otherwise False is returned

    Args:
        x (int): Any integer

    Returns:
        bool: True if x is an integer, otherwise False is returned

    """
    return type(x) == int


def is_list(x):
    """Returns True is x is a list, otherwise False is returned

    Args:
        x (list): Any list

    Returns:
        bool: True if x is a list, otherwise False is returned

    """
    return type(x) == list


def has_whitespace(x):
    """Returns True if x is a string that has whitespace, otherwise False is returned

    Args:
        x (string): Any string

    Returns:
        bool: True if x is a string that has whitespace, otherwise False is returned

    """
    if is_str(x) and re.search('\s+', x):
        return True
    return False
