# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons = [
    {
        "name": "bob",
        "age": 81,
        "hobbies": "coding"
    },
    {
        "name": "joe",
        "age": 22,
        "hobbies": "fishing"
    },
    {
        "name": "jack",
        "age": 55,
        "hobbies": "golfing"
    },

]
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
just_names = [person['name'] for person in persons]
print(just_names)
# 3) Use a list comprehension to check whether all persons are older than 20.

older_twenty = all([person['age'] > 20 for person in persons])
print(older_twenty)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
safe_copy = [person.copy() for person in persons]
safe_copy[0]['name'] = 'notbob'
print(safe_copy)
print(persons)
# 5) Unpack the persons of the original list into different variables and output these variables.
a, b, c = persons
print(a)
print(b)
print(c)
