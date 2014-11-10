"""Tracks allergies"""

class Allergies(object):
    """Generates and stores allergies from a given score"""

                   # Allergie       # score
    allergie_list = ['eggs',        # 1
                     'peanuts',     # 2
                     'shellfish',   # 4
                     'strawberries',# 8
                     'tomatoes',    # 16
                     'chocolate',   # 32
                     'pollen',      # 64
                     'cats',        # 128
                    ]

    def __init__(self, score):
        """Generates a list of allergies from a score"""
        self.list = []
        # Reverse the binary of the score (i.e. '0b10010' is bin(18))
        # skip the '0b' part and use bits to select allergies from the list
        for bit, allergie in zip((bin(score))[:1:-1], Allergies.allergie_list):
            if bit == '1':
                self.list.append(allergie)

    def is_allergic_to(self, allergie):
        """Tests if allergie is on the list"""
        return allergie in self.list
