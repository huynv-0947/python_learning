# assign variable
one = 1
two, three, name = 2, 3, 'sherlock'

print(one, two, three)
print(name)

# numbers
print(0x1 + 4)
print(0xAA - 70 + 0.25)

# strings
strs = "Ruby on Rails"
print(strs[0], strs[0:], strs[0:4], strs + "!")

# lists
count = [1, 2, 'three', 'four']
print(count, count[0], count[0:2])

# tuples
tuples = (1, 2, 'three', 'four')
# error syntax: tuples[0] = 0
print(tuples, tuples[0], tuples[0:2])

# set
sets = {1, 2, 3}
sets.add(1)
print(sets) # {1, 2, 3}
sets.add(4)
print(sets) # {1, 2, 3, 4}

# dictionary
dict = {"one": 1, 2: "two"}
print(dict, dict['one'], dict[2], dict.keys(), dict.values())

# conversion
print(int("10"), int("10", 2), float("0.25"), complex(1, 2), complex(0, 2))
print(str('python'), repr('python'))
print(tuple("12345xxx"))
