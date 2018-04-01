def rebase(input_base, digits, output_base):
    return to_base(from_base(digits, input_base), output_base)

def from_base(digits, base):
    result = 0
    if base < 2:
        raise ValueError("Not a valid base: {}".format(base))
    for digit in digits:
        if not (0 <= digit < base):
            raise ValueError("Not a valid digit in base {}: {}".format(base, digit))
        result = result * base + digit
    return result

def to_base(number, base):
    digits = []
    if base < 2:
        raise ValueError("Not a valid base: {}".format(base))
    while number > 0:
        digits.insert(0, number % base)
        number //= base
    return digits
