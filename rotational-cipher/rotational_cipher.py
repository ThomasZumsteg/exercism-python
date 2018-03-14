def rotate(text, key):
    def rot(letter):
        if letter.islower():
            return chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
        if letter.isupper():
            return chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
        return letter
    return ''.join(rot(l) for l in text) 
