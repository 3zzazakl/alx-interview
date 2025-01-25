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
    n_bytes = 0

    for num in data:
        bin_repr = format(num, '#010b')[-8:]

        if n_bytes == 0:
            for bit in bin_repr:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_repr[0] == '1' and bin_repr[1] == '0'):
                return False

        n_bytes -= 1

    return n_bytes == 0
