"""String transform functions"""

import string
import check

def camelcase_to_underscore(s):
    """Convert a CamelCase string to lowercase string separated by underscore

    Args:
        s (str): CamelCase string (no whitespace)

    Returns:
        (str): Lowercase string separated by underscore

    """
    assert check.has_whitespace(s) == False, 'String must not have any whitespace'
    caps = string.ascii_uppercase
    new_str = s[0].lower()
    for c in s[1:]:
        if c in caps:
            new_str += '_' + c.lower()
        else:
            new_str += c
    return new_str