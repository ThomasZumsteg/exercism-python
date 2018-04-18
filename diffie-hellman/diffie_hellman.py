import random

def private_key(p):
    return random.choice(range(2, p))


def public_key(p, g, private):
    return pow(g, private, p)


def secret(p, public, private):
    return pow(public, private, p)
