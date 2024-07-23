some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

check_list = []
duplicates = set()

for item in some_list:
    if item in check_list:
        duplicates.add(item)
    check_list.append(item)

print('The following values are duplicates: ' + str(duplicates))
