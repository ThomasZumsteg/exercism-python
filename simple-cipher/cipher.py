"""Cipher based shift methods"""
from string import ascii_lowercase
from random import choice

class Cipher(object):
    """Implementation of a key shift cipher"""

    def __init__(self, key=None):
        """Use a custom key or a random string of 100 lower case characters"""
        if key:
            self.key = key
        else:
            self.key = ''.join([choice(ascii_lowercase) for _ in range(100)])

    def encode(self, clear_text):
        """Encodes text using key"""
        key_func = self._inf_iter([ord(c)-97 for c in self.key])
        return self._shift(clear_text, key_func)

    def decode(self, cipher_text):
        """Decodes text using key"""
        key_func = self._inf_iter([-ord(c)+97 for c in self.key])
        return self._shift(cipher_text, key_func)

    @staticmethod
    def _shift(text, key_func):
        """Shifts characers in text according to a key function"""
        text = [c for c in text.lower() if c.isalpha()]
        shift_dist = lambda x, s: chr((ord(c)-97+s) % 26 + 97)
        return ''.join([shift_dist(c, k) for c, k in zip(text, key_func)])

    @staticmethod
    def _inf_iter(key):
        """Turns a key in to an infitite iterator"""
        while True:
            for i in key:
                yield i

class Caesar(Cipher):
    """A Caesarian shift cipher"""

    def __init__(self):
        """A constant distance shift cipher"""
        super(Caesar, self).__init__("d")
