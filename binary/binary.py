"""Converts binary string to integer"""

def parse_binary(binary):
    """converts string of 1 and 0 to integer"""
    num = 0
    for bit in binary:
        num <<= 1
        if bit == "1":
            num |= 1
        elif bit != "0":
            raise ValueError
    return num
