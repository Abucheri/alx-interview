#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing byte data.

    Returns:
        True if data is a valid UTF-8 encoding, else returns False
    """
    # Check if data is a list
    if not isinstance(data, list):
        return False

    # Check if all elements in data are integers
    if not all(isinstance(byte, int) for byte in data):
        return False

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        bit = 1 << 7
        if num_bytes == 0:
            # Count the number of bytes in this UTF-8 character
            while (bit & byte):
                num_bytes += 1
                bit = bit >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If it's a continuation byte
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        num_bytes -= 1
    # If there are remaining bytes left
    return num_bytes == 0
