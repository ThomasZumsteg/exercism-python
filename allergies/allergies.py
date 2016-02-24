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
        self.lst = [allergie
                    for i, allergie in enumerate(Allergies.allergie_list)
                    if 0 < (score & 1 << i )]

    def is_allergic_to(self, allergie):
        """Tests if allergie is on the list"""
        return allergie in self.lst
