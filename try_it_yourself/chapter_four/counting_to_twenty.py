# 4-3. Counting to 20
"""
for number in range(1, 21):
    print(number)
"""
# 4-4. One million
numbers = []
for number in range(1, 1000001):
    numbers.append(number)
# print(numbers)
# 4-5. Summing a million
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# 4-6. Odd numbers
"""
numbers = []
for number in range(1, 21):
    numbers.append(number)
print(numbers)
for number in numbers:
    print(number)
    """
# 4-7. Threes

numbers = []
for number in range(0, 31, 3):
    numbers.append(number)
for number in numbers:
    print(number)

# 4-8. Cubes
"""
cubes = []
for cube in range(1, 11):
    cubes.append(cube ** 3)
print(cubes)
for cube in cubes:
    print(cube)
    """
# 4-9. Cube comprehension
cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)
