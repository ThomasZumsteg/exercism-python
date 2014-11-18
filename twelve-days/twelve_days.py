"""Sings the twelve days of christmas"""

def sing():
    """Sings the twelve days of chirstmas"""
    return verses(1, 12)

def verses(start, stop):
    """Sings several verses of the twelve days of christmas"""
    return "\n".join(verse(n) for n in range(start, stop+1)) + "\n"

def verse(v):
    """Sings a verse of the twelve days of christmas"""
    if v == 1:
        # Stupid "and a"!!!!
        return "On the first day of Christmas my true love gave to me, " \
                "a Partridge in a Pear Tree.\n"

    nums = ["first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth" ]
    gifts = ["and a Partridge in a Pear Tree",
             "two Turtle Doves",
             "three French Hens",
             "four Calling Birds",
             "five Gold Rings",
             "six Geese-a-Laying",
             "seven Swans-a-Swimming",
             "eight Maids-a-Milking",
             "nine Ladies Dancing",
             "ten Lords-a-Leaping",
             "eleven Pipers Piping",
             "twelve Drummers Drumming",
            ]
    start = "On the %s day of Christmas my true love gave to me"
    return ", ".join([start % nums[v-1]] + gifts[v-1::-1]) + ".\n"
