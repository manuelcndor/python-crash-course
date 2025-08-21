# To make a slice, you have to specify the index of the first and last
# elements you want to work with.


russian_cities = ["Moscow", "Saint Petersburg",
                  "Perm", "Vladivostok", "Volgograd"]

print(russian_cities[:2])

# you can include a third value and tell Python how many items to skip.
# Looping through a slice
print("Here are the first 2 cities from my list:")
for city in russian_cities[0:2]:
    print(city)
