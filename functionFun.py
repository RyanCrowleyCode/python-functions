#LIST
stuff = ["name", "age", "address", "phone"]

#1 good old for loop example
cap_stuff = []
for foo in stuff:
    cap_stuff.append(foo.capitalize())

#2 map example
cap_stuff = list(map(lambda foo: foo.capitalize(), stuff))

#3 comprehension
cap_stuff = [foo.capitalize() for foo in stuff]


# DICTIONARY
profile = {
    "name": "Fred",
    "age": 34,
    "address": "123 Sesame St"
}

# for loop version
profile_strings = []
for key, value in profile.items():
    profile_strings.append(f"The key is {key}. The value is {value}")

# comprehension
profile_strings = [ f"The key is {key}. The value is {value}" for key, value in profile.items() ]
print(profile_strings)