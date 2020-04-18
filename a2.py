# 1) Create a list of names and use a for loop to output the length of each name (len() ).
names = ['bob', 'mike', 'joe', 'braddley', 'nicholas', 'nancy']


def print_names(arr):
    for name in names:
        # 2) Add an if  check inside the loop to only output names longer than 5 characters.
        if len(name) > 5:
            print(name)
        # 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
        if 'n' in name or 'N' in name:
            print(name)


# 4) Use a while  loop to empty the list of names (via pop() )
def clear_list(arr):
    not_empty = True

    while not_empty:
        if len(names) == 0:
            not_empty = False
            return not_empty
        names.pop()


print_names(names)
clear_list(names)
print(names)
