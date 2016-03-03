NUMBERS = [''] + 'one two three four five six seven eight nine'.split()
TENS = [''] + 'ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
TEENS = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()

POWERS = [''] + ' thousand- million- billion'.split('-')

def say(num):
    """say constructs the english phrase for a number between 0 and one trillion"""

    if not (0 <= num < 1E12):
        raise AttributeError("Number must be between 0 and one trillion")
    if num == 0:
        return 'zero'

    p = -1
    number = ''
    while num > 0:
        p += 1
        num, power = divmod(num, 1000)
        if power == 0:
            continue

        str_pow = say_power(power) + POWERS[p]

        if p == 0 and 0 < power < 100 and num != 0:
            number = 'and ' + str_pow
        elif number == '':
            number = str_pow
        else :
            number = str_pow + ' ' + number
    return number

def say_power(num):
    """say_power converts a number between 1 and 999 to the english phrase"""
    hundereds, tens, ones = int(num // 100), int((num % 100) // 10), int(num % 10)
    number = ''
    if hundereds != 0:
        number += '{} hundred'.format(NUMBERS[hundereds])
        if tens == 0 and ones == 0:
            return number
        number += ' and '

    if tens == 1:
        return number + TEENS[ones]
    if tens != 0:
        number += TENS[tens]
        if ones == 0:
            return number

    if number == '':
        return NUMBERS[ones]
    return number + '-' + NUMBERS[ones]

