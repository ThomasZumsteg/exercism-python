"""Creates and decodes binary handshakes from Mary Poppins"""

def binary(func):
    """Decorator to force correct string into handshake"""
    def force_binary(secret):
        """force binary string"""
        if type(secret) != int:
            try:
                secret = int(secret, 2)
            except ValueError:
                secret = 0
        if secret < 0:
            secret = 0
        return func(format(secret, "05b")[::-1])
    return force_binary

@binary
def handshake(secret):
    """Decodes binary handshake"""
    steps = ["wink", "double blink", "close your eyes", "jump"]
    to_do = []
    for bit, action in zip(secret, steps):
        if bit == "1":
            to_do.append(action)
    if secret[-1] == "1":
        to_do.reverse()
    return to_do

def code(shake):
    """Creat binary handshake"""
    values = ("wink", "double blink", "close your eyes", "jump")
    secret = 0
    for action in shake:
        if action not in values:
            return '0'
        secret |= 2 ** values.index(action)
    if shake and values.index(shake[0]) > values.index(shake[-1]):
        secret |= 16
    return format(secret, "b")
