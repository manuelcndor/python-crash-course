

# The sorted() function maintains the original order of a list but prints it in
# sorted order.

cities = ["Moscow", "Saint Petersburg", "Perm", "Vladivostok", "Volgograd"]

print("Here's the original list.")
print(cities)

print("\nHere's the sorted list.")
print(sorted(cities))

print("\nHere's the original lis again.")
print(cities)

print("\nThis function also accepts a reverse=True argument.")
print(sorted(cities, reverse=True))
