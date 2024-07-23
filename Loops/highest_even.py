def highest_even(li: list) -> int:
    highest_number = min(li)
    for number in li:
        if number > highest_number and number % 2 == 0:
            highest_number = number
    if highest_number % 2 != 0:
        return 'No even number found'
    else:
        return f'Highest even number is: {highest_number}'


print(highest_even([1, 123, 43, 3, 111, 5, 7]))
