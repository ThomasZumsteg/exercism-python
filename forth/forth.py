class StackUnderflowError(Exception):
    pass


keywords = {
    '+': (2, lambda a, b: (a + b,)),
    '-': (2, lambda a, b: (a - b,)),
    '*': (2, lambda a, b: (a * b,)),
    '/': (2, lambda a, b: (a // b,)),
    'swap': (2, lambda a, b: (b, a)),
    'over': (2, lambda a, b: (a, b, a)),
    'dup': (1, lambda x: (x, x)),
    'drop': (1, lambda x: tuple()),
    }


def evaluate(input_data):
    tokens = [token for line in input_data for token in line.split()]
    stack = []
    env = {}
    while tokens:
        token = tokens.pop(0).lower()
        if token == ':':
            keyword = tokens.pop(0).lower()
            if keyword.isdigit():
                raise ValueError("Variables cannot be numbers: " + keyword)
            env[keyword] = [tokens.pop(0)]
            while env[keyword][-1] != ';':
                env[keyword].append(tokens.pop(0))
            env[keyword].pop()
        elif token in env:
            tokens.extend(env[token])
        elif token in keywords:
            try:
                n_args, func = keywords[token]
                args = tuple(reversed([stack.pop() for _ in range(n_args)]))
                stack.extend(func(*args))
            except IndexError:
                raise StackUnderflowError('Cannot apply ' + token)
        else:
            stack.append(int(token))
    return stack
