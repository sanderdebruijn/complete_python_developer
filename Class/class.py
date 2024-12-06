# OOP practice

class PlayerCharacter:
    membership = True  # class object attribute

    def __init__(self, name='anonymous', age=0):
        if (age >= 18):  # Only allow creation of a player when they are older than 18
            self.name = name
            self.age = age

    def run(self):
        print('run')


player1 = PlayerCharacter('Sander', 25)

print(player1.name)
player1.run()
print(player1.membership)

# Exercise

# Given the below class:


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat_one = Cat('Bella', 12)
cat_two = Cat('Rodrigo', 13)
cat_three = Cat('Oeua', 13)

# 2 Create a function that finds the oldest cat and use it


def find_oldest_cat(cat_objects: list):
    for cat_object in cat_objects:
        max_age = 0
        if cat_object.age > max_age:
            max_age = cat_object.age
        else:
            pass
    for cat_object in cat_objects:
        if cat_object.age == max_age:
            print(f'{cat_object.name} is (one of) the oldest cat(s), they are {cat_object.age} years old')  # noqa
        else:
            pass


find_oldest_cat([cat_one, cat_two, cat_three])
