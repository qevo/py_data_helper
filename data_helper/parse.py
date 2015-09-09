"""String parse wrapper functions to streamline common use cases"""

import re
from check import is_list, is_str, is_bool, is_str_not_empty, is_int_pos


def str_split_size(s, n=None):
    """Split a string by length

    Args:
        s (str): The string to be divided. Value type is converted to string.
        n (int): Length of string per list item. Value type is converted to integer.

    Returns:
        list: List of strings, each the same size, in the same order as they appear in the string.

    """
    s = str(s)
    n = int(n) if n else int(len(s) / 2)

    if not is_str_not_empty(s): raise ValueError("'s' must be a non empty string")
    if not is_int_pos(n): raise ValueError("'n' must be a positive integer")

    return [s[start:start + n] for start in range(0, len(s), n)]


def str_split_caps(s, trim=True):
    """Split a string on capital letters

    Args:
        s (str): The string to be divided. Value type is converted to string.
        trim (bool): Remove whitespace. Defaults to True.

    Returns:
        list: List of strings, each starting with a capital letter, in the same order as they appear in the string.

    """
    if not is_str(s): raise TypeError("'s' must be a string")
    if not is_bool(trim): raise TypeError("'trim' must be True or False")

    result = re.findall('[A-Z][^A-Z]*', s)
    if trim:
        result_trim = []
        for w in result:
            result_trim.append(w.strip())
        result = result_trim
    return result


def list_filter(pattern, iter, flags=0):
    """Use regular expression patterns to filter a list of strings

    Args:
        pattern (str|list): String or list of strings of regular expression patterns.
        iter (list): List of strings to be filtered. Can be any iterable object that can be iterated in a for-loop.
        flags (int): See :py:mod:`re`

    Returns:
        list: List of matching strings.

    """
    if is_list(pattern):
        pass
    elif is_str(pattern):
        pattern = [pattern]
    else:
        raise TypeError("'pattern' must be a string or list of strings")

    if not is_list(iter):
        raise TypeError("'iter' must be a list of strings")

    re_filters = []
    for p in pattern:
        re_filters.append(re.compile(p, flags))

    matches = []
    for s in iter:
        for f in re_filters:
            if f.match(s):
                matches.append(s)
                break
    return matches
