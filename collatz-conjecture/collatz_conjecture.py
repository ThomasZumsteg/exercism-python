from itertools import count 

def collatz_steps(number):
    if number <= 0:
        raise ValueError(
                "Number must be greater then 0: collatz_steps({})".format(number))
    for step in count(0):
        if number == 1:
            return step
        number = number / 2 if number % 2 == 0 else 3 * number + 1
