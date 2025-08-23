
# A tuple is an immutable list.

dimensions = (24, 40)

print(dimensions[1])
print(dimensions[0])

# Tuples do not support item assignment

# dimensions[0] = 50

# print(dimensions)

# Tuples are technically defined by the presence of a comma. If you want to
# define a tuple with one element, you need to include a trailing comma.
"""
favorite_number = 27,
print(favorite_number[0])
"""
# Looping
favorite_numbers = (27, 14, 26, 30)
for number in favorite_numbers:
    print(number)
