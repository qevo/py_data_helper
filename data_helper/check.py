"""Check for a condition"""

import re


def is_bool(x):
    """Returns True if x is boolean, otherwise False is returned

    Args:
        x (bool): True | False

    Returns:
        bool: True if x is boolean, otherwise False is returned

    """
    return type(x) == bool


def is_str(x):
    """Returns True if x is a string, otherwise False is returned

    Args:
        x (string): Any string

    Returns:
        bool: True if x is a string, otherwise False is returned

    """
    return type(x) == str


def is_str_empty(x):
    """Returns True if x is a string that is empty, otherwise False is returned

    Args:
        x (string): Any string

    Returns:
        bool: True if x is a string that is empty, otherwise False is returned

    """
    return True if is_str(x) and x == '' else False


def is_str_not_empty(x):
    """Returns True if x is a string that is not empty, otherwise False is returned

    Args:
        x (string): Any string

    Returns:
        bool: True if x is a string that is not empty, otherwise False is returned

    """
    return True if is_str(x) and x != '' else False


def is_int(x):
    """Returns True if x is an integer, otherwise False is returned

    Args:
        x (int): Any integer

    Returns:
        bool: True if x is an integer, otherwise False is returned

    """
    return type(x) == int


def is_int_not_neg(x):
    """Returns True if x is zero or a positive integer, otherwise False is returned

    Args:
        x (int): Any integer

    Returns:
        bool: True if x is zero of a positive integer, otherwise False is returned

    """
    return True if is_int(x) and x >= 0 else False


def is_int_pos(x):
    """Returns True if x is a positive integer, otherwise False is returned

    Args:
        x (int): Any integer

    Returns:
        bool: True if x is a positive integer, otherwise False is returned

    """
    return True if is_int(x) and x > 0 else False


def is_int_neg(x):
    """Returns True if x is a negative integer, otherwise False is returned

    Args:
        x (int): Any integer

    Returns:
        bool: True if x is a negative integer, otherwise False is returned

    """
    return True if is_int(x) and x < 0 else False


def is_list(x):
    """Returns True if x is a list, otherwise False is returned

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
