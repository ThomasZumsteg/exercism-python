from itertools import permutations

def solution():
    """Finds solutions to the zebra puzzle"""
    solutions = list(zebra_puzzle())
    assert(len(solutions) == 1)
    return ("It is the %s who drinks the water.\n"
        "The %s keeps the zebra." %(solutions[0]['water'], solutions[0]['zebra']))

def zebra_puzzle():
    """Iterator that finds all solutions to the zebra puzzle"""
    residents = 'Englishman, Spaniard, Ukranian, Japanese, Norwegian'.split(', ')
    orderings = list(permutations(residents))
    first, _, middle, _, _ = (0, 1, 2, 3, 4)

    for (red, green, ivory, yellow, blue) in orderings:
        if red != 'Englishman':
            continue
        for order in orderings:
            if abs(order.index('Norwegian') - order.index(blue)) != 1:
                continue
            if order[0] != 'Norwegian':
                continue
            if order.index(green) - order.index(ivory) != 1:
                continue
            for (dog, snails, fox, horse, ZEBRA) in orderings:
                if dog != 'Spaniard':
                    continue
                for (coffee, tea, milk, oj, WATER) in orderings:
                    if order.index(milk) != middle:
                        continue
                    if coffee != green:
                        continue
                    if tea != 'Ukranian':
                        continue
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:
                        if OldGold != snails:
                            continue
                        if Kools != yellow:
                            continue
                        if abs(order.index(Chesterfields) - order.index(fox)) != 1:
                            continue
                        if abs(order.index(Kools) - order.index(horse)) != 1:
                            continue
                        if LuckyStrike != oj:
                            continue
                        if Parliaments != 'Japanese':
                            continue
                        yield { 'zebra': ZEBRA, 'water': WATER }

