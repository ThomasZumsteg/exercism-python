"""Does a natrual language calculation"""
from operator import add, sub, mul, truediv
from re import finditer, match

def calculate(string):
    """Parses and preforms natrual language calculation"""
    operators = {"plus": add,
                 "minus": sub,
                 "multiplied by": mul,
                 "divided by": truediv,
                }
    start = "What is"
    function = " (" + "|".join(operators.keys()) + ")"
    number = r" (-?\d+)"
    regex = start + "(?P<first>" + number + ")" + "(?P<calculation>" +\
            "(" + function + number + ")+)" + r"\?$"
    regex_match = match(regex, string)
    if not regex_match:
        raise ValueError
    val = int(regex_match.group('first'))
    remaining = regex_match.group('calculation')
    for step in finditer(function + number, remaining):
        (func, num) = step.groups()
        val = operators[func](val, int(num))
    return val
