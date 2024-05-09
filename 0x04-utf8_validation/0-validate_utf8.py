#!/usr/bin/python3
"""
Module for UTF-8 validation
---------------------------
This function efficiently iterates through the input data, identifying start
bytes and continuation bytes according to the UTF-8 encoding rules, and
ensuresthat they are correctly paired.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    The for loop iterates over each integer in the data list. num_bytes is
    initialized to 0 and will keep track of how many continuation bytes
    are expected for the current UTF-8 character.
    For each integer byte, the code checks if it represents the start byte
    of a UTF-8 character. It does so by checking the leftmost
    (most significant) bit of the byte. If it's set to 1, it indicates the
    start of a UTF-8 character. The loop counts the number of leading 1 bits
    to determine the number of bytes in the character.
    If num_bytes is not 0, it means the current byte is a continuation byte.
    After processing each byte, whether it's a start byte or a continuation
    byte, num_bytes is decremented. This indicates that we've processed one
    byte in the current UTF-8 character.
    Finally, after processing all bytes in data, we check if num_bytes is back
    to 0. If it's not, it means there are remaining bytes left without a
    corresponding start byte, which indicates invalid UTF-8 encoding.
    If nbytes is 0, it means all bytes were properly paired, and the function
    returns True, indicating valid UTF-8 encoding.

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
        # This section of code checks if it represents the start byte of
        # a UTF-8 character
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
            # This section checks if the current byte follows the pattern
            # 10xxxxxx, which is characteristic of a continuation byte in
            # UTF-8 encoding
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        # Decrementing num_bytes
        num_bytes -= 1
    # If there are remaining bytes left
    return num_bytes == 0
