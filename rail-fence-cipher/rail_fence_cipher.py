def encode(message, rails):
    return ''.join(_make_rails(message, rails))

def decode(encoded_message, rails):
    message = [None for _ in range(len(encoded_message))]
    for i, e in enumerate(_make_rails(range(len(encoded_message)), rails)):
        message[e] = encoded_message[i]
    return ''.join(message)

def _make_rails(items, rails):
    rail_lists = [[] for _ in range(rails)]
    step, rail = 1, 0
    for char in items:
        rail_lists[rail].append(char)
        if not (0 <= rail + step < rails):
            step *= -1
        rail += step
    return tuple(item for sublist in rail_lists for item in sublist)
