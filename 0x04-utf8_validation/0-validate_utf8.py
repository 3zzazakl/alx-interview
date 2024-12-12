#!/usr/bin/python3
"""
Validate UTF-8 string
"""


def validUTF8(data):
    """
    Validate UTF-8 string
    :param data: string to validate to be UTF-8
    :return: True if valid UTF-8, False otherwise
    """
    i = 0
    n = len(data)

    while i < n:
        byte = data[i]

        if byte & 0x80 == 0:
            i += 1
        elif byte & 0xE0 == 0xC0:
            if i + 1 >= n or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        elif byte & 0xF0 == 0xE0:
            if (i + 2 >= n
                or data[i + 1] & 0xC0 != 0x80
                    or data[i + 2] & 0xC0 != 0x80):
                return False
            i += 3
        elif byte & 0xF8 == 0xF0:
            if (
                i + 3 >= n
                or data[i + 1] & 0xC0 != 0x80
                or data[i + 2] & 0xC0 != 0x80
                or data[i + 3] & 0xC0 != 0x80
            ):
                return False
            i += 4
        else:
            return False

    return True
