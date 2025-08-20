# You can use the range() function to print a series of numbers.
"""
for value in range(1, 50):
    print(value)
"""
"""
numbers = list(range(1, 5))
print(numbers)
"""
# If you add a third argument to range(), Python is going to use that number
# as a step size.
"""
even_numbers = list(range(0, 11, 2))
print(even_numbers)
"""
# Square numbers

squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# It is useful to work with some functions
# To find the minimum
print(min(squares))
# To find the maximum
print(max(squares))
# To find the sum
print(sum(squares))
