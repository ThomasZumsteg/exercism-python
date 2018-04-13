from collections import Counter


def count_func(num):
    return lambda dice: num * Counter(dice)[num]


def four_of_a_kind(dice):
    for k, v in Counter(dice).items():
        if 4 <= v:
            return k * 4
    return 0


def straight(dice):
    min_dice = min(dice)
    length = 1
    while min_dice + length in dice:
        length += 1
    return length


# Score categories
# Change the values as you see fit
YACHT = lambda dice: 50 if len(dice) == 5 and len(set(dice)) == 1 else 0
ONES = count_func(1)
TWOS = count_func(2)
THREES = count_func(3)
FOURS = count_func(4)
FIVES = count_func(5)
SIXES = count_func(6)
FULL_HOUSE = lambda dice: sum(dice) if \
    sorted(tuple(Counter(dice).values())) == [2, 3] else 0
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = lambda dice: 30 if 5 == straight(dice) and max(dice) == 5 else 0
BIG_STRAIGHT = lambda dice: 30 if 5 == straight(dice) and max(dice) == 6 else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)

