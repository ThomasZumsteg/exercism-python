CHECK_BIT = 0x80

def encode(numbers):
    result = []
    for number in reversed(numbers):
        result.insert(0, 0x00)
        while True:
            result[0] |= number & (CHECK_BIT - 1)
            number >>= 7
            if number <= 0:
                break
            result.insert(0, CHECK_BIT)
    return result


def decode(bytes_):
    results = []
    value = 0
    for byte in bytes_:
        value = (value << 7) | byte & ~(CHECK_BIT)
        if byte & CHECK_BIT <= 0:
            results.append(value)
            value = 0
    if byte & CHECK_BIT == 0:
        return results
    raise ValueError("Not a valid bit stream")
