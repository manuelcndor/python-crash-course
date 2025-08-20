

# List comprehension = A concise way to create lists in Python
#                      Compact  and easier to read than a traditional loop
#                      [expression for value in iterable if condition]

doubles = []
for double in range(1, 11):
    doubles.append(double * 2)
print(doubles)

doubles = [double * 2 for double in range(1, 11)]
print(doubles)

# triples

triples = [triple * 3 for triple in range(1, 11)]
print(triples)

# Squares

squares = [square ** 2 for square in range(1, 11)]
print(squares)

# Cubes

cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)

# To the power of 100

one_hundred = [x ** 100 for x in range(1, 11)]
print(one_hundred)
