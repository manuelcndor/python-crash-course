# 4-10.
"""
animals = ["cat", "dog", "hamster", "snake", "mouse", "parrot", "tortoise",
           "minipig", "cow"]

print("The first three items in the list are: ")
for animal in animals[0:3]:
    print(animal.capitalize())
print("Three items from the middle of the list are: ")
for animal in animals[3:6]:
    print(animal.capitalize())
print("The last three items in the list are: ")
for animal in animals[6:9]:
    print(animal.capitalize())
"""
# 4-11.My pizzas, your pizzas
"""
types_of_pizza = ["pepperoni", "american", "hawaian"]
friend_pizzas = types_of_pizza[:]

types_of_pizza.append("napolitan")
print("My favorite pizzas are: ")
for pizza in types_of_pizza:
    print(pizza)

friend_pizzas.append("peruvian")
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
"""
# 4-12. Choose a version of food.py and write two for loops to print each
# list of foods.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are: ")
for food in my_foods:
    print(food.capitalize())

print("\nMy friend's favorite foods are: ")
for food in friend_foods:
    print(food.capitalize())
