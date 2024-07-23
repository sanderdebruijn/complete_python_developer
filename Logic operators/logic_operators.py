is_magician = False
is_expert = True

# Way 1 using conditional logic (cleanest for this specific use-case)
if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('At least you\'re getting there')
else:
    print('You need magic powers')

# Way 2 using ternary operator
print('You are a master magician') if is_magician and is_expert else (
    print('At least you\'re getting there') if is_magician and not is_expert else (
        print('You need magic powers')
    )
)


# Way 1 in a function
def check_magician(is_magician: bool, is_expert: bool) -> str:
    if is_magician and is_expert:
        print('You are a master magician')
    elif is_magician and not is_expert:
        print('At least you\'re getting there')
    else:
        print('You need magic powers')


check_magician(is_magician=True, is_expert=False)


# Way 1 in a function
def check_magician_input() -> str:
    is_magician = int(input('Are you a magician? 1 or 0   '))
    is_expert = int(input('Are you an expert? 1 or 0   '))
    if is_magician and is_expert:
        print('You are a master magician')
    elif is_magician and not is_expert:
        print('At least you\'re getting there')
    else:
        print('You need magic powers')


check_magician_input()
