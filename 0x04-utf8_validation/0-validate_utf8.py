#!/usr/bin/python3
"""
the validation checker utf-8
"""


def validUTF8(data):
    """
    Validate if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers, where each integer represents a byte.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of continuation bytes expected

    # Masks for extracting the first few bits of each byte
    mask1 = 1 << 7       # 10000000
    mask2 = 1 << 6       # 01000000

    for byte in data:
        # Apply only the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:  # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == mask1:  # 2-byte character
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 | mask2):  # 3-byte character
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 | mask2 | (mask1 >> 2)):
                num_bytes = 3
            else:
                return False
        else:
            # Continuation byte check: it should start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
