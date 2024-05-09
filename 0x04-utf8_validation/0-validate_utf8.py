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
        boolean: True if data is a valid UTF-8 encoding, else returns False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If it's the start of a new character
        if num_bytes == 0:
            # Count the number of bytes in this UTF-8 character
            if byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 7 == 1:
                return False
        else:
            # If it's a continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
    # If there are remaining bytes left
    return num_bytes == 0
