"""Encipher a message using a crypto square"""
from math import ceil

def encode(clear_text):
    """Encipher a message using a crypto square"""
    clear_text = [c for c in clear_text.lower() if c.isalnum()]
    square_size = int(ceil(len(clear_text)**0.5))
    cipher_text = [clear_text[i::square_size] for i in range(square_size)]
    return ' '.join([''.join(text) for text in cipher_text])
