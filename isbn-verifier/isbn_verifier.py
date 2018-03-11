def verify(isbn):
    counter = 1
    total = 0
    for d in reversed(isbn):
        if d is 'X':
            if counter != 1:
                return False
            d = '10'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0
