def binary_search(list_of_numbers, number):
    start, end = 0, len(list_of_numbers) - 1
    while start <= end:
        middle = (start + end) // 2
        if number > list_of_numbers[middle]:
            start = middle + 1
        elif number < list_of_numbers[middle]:
            end = middle - 1
        else:
            return middle
    raise ValueError("{} not in list".format(number))
