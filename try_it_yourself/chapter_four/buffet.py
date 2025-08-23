

# 4-13.

menu = ("ceviche", "chaufa", "papa rellena",
        "lomo saltado", "pollo a la brasa")

print("This is the menu: ")
for food in menu:
    print(food.capitalize())

# We cannot modify a tuple
# menu[2] = "tallarines rojos"
# print(menu[2])

menu = ("ceviche de conchas negras", "aeropuerto", "papa rellena",
        "lomo saltado", "pollo a la brasa")

print(f"\nThis is the new menu: ")
for food in menu:
    print(food.capitalize())
