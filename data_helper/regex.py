"""Regular expressions wrapper functions to streamline common use cases"""


def wildcard_re(pattern, wildcard='*', escape='\\'):
    """Transform a wildcard pattern to a regular expressions pattern

    Alphanumeric characters are preserved. All other characters are escaped
    except for asterisk which is replaced with '.*'

    Args:
        pattern (str): String of wildcard pattern.
        wildcard (str): Wildcard symbol. Defaults to '*'
        escape (str): Character escape symbol (must be a Python string literal). Defaults to '\\'

    Returns:
        str: Regular expressions pattern.

    """
    if type(pattern) != str:
        raise TypeError("'pattern' must be a string")
    if type(wildcard) != str:
        raise TypeError("'wildcard' must be a string")
    if type(escape) != str:
        raise TypeError("'escape' must be a string")

    new_str = ''
    for c in pattern:
        if c.isalnum():
            new_str += c
        elif c == wildcard:
            new_str += '.' + c
        else:
            new_str += escape + c
    return new_str
