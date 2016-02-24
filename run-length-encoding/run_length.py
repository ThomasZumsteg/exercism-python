from re import findall

def encode(text):
    """encode compresses text by replacing repeated characters
    with number of repeates and the character"""
    return ''.join(
        "%d%s" % (len(letters), letter) if len(letters) > 1 else letter
        for letters, letter in findall(r'((.)\2*)', text))

def decode(compressed):
    """decode uncompresses text but expanding repeated characters"""
    return ''.join(
        int(count) * letter if count else letter
        for count, letter in findall('(\d*)(.)', compressed ))
