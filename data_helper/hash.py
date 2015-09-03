"""Data hashing helper

This module provides regular expressions wrapper functions to streamline common use cases.

"""

import hashlib


def py(*args):
    """Wrap the python hash() function

    Args:
        args (str): Object to be hashed. See :py:func:`hash`

    Returns:
        int: Hash value

    """
    return hash(*args)


def md5(data):
    """Return the MD5 hash

    Args:
        data (str): Data to be hashed.

    Returns:
        str: Hexadecimal hash string.

    """
    return hashlib.md5(data).hexdigest()


def sha1(data):
    """Return the SHA1 hash

    Args:
        data (str): Data to be hashed.

    Returns:
        str: Hexadecimal hash string.

    """
    return hashlib.sha1(data).hexdigest()


def sha224(data):
    """Return the SHA224 hash

    Args:
        data (str): Data to be hashed.

    Returns:
        str: Hexadecimal hash string.

    """
    return hashlib.sha224(data).hexdigest()


def sha256(data):
    """Return the SHA256 hash

    Args:
        data (str): Data to be hashed.

    Returns:
        str: Hexadecimal hash string.

    """
    return hashlib.sha256(data).hexdigest()


def sha384(data):
    """Return the SHA384 hash

    Args:
        data (str): Data to be hashed.

    Returns:
        str: Hexadecimal hash string.

    """
    return hashlib.sha384(data).hexdigest()


def sha512(data):
    """Return the SHA512 hash

    Args:
        data (str): Data to be hashed.

    Returns:
        str: Hexadecimal hash string.

    """
    return hashlib.sha512(data).hexdigest()
