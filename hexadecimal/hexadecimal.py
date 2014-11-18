"""Converts hex string to decimal number"""

def hexa(hex_num):
    """Converts hex string to decimal number"""
    h_dict = dict(zip("0123456789abcdef", range(16)))
    dec_num = 0
    for char in hex_num.lower():
        dec_num <<= 4
        try:
            dec_num |= h_dict[char]
        except KeyError:
            raise ValueError
    return dec_num
