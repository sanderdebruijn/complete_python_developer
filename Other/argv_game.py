import sys
from random import randint


def number_input():
    number = int(input(f"Please guess a number from {min} and {max}: "))
    return number


min = int(sys.argv[1])
max = int(sys.argv[2])

if max <= min:
    print("Please supply an upper bound higher than the lower bound")
    ValueError

number = randint(min, max)
guess = number_input()

while number != guess:
    print("Wrong answer, try again.")
    guess = number_input()

print(f"Good job! The number was {number}")
