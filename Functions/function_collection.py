from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capi(item):
    return item.upper()


print(list(map(capi, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

combination = list(zip(my_strings, sorted(my_numbers)))
print(combination)


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def above50(item):
    return item > 50


print(list(filter(above50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total? # noqa


def accumulator(acc, item):
    return acc + item


all_numbers = scores + my_numbers

print(reduce(accumulator, all_numbers, 0))

# Square all numbers in a list with lambda
square_list = [3, 4, 5]

print(list(map(lambda item: item**2, square_list)))

# list sorting (with lamda)
sort_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

sort_list.sort(key=lambda x: x[1])
print(sort_list)
