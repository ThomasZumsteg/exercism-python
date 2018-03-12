def is_armstrong(number):
    return sum(int(d)**len(str(number)) for d in str(number)) == number
