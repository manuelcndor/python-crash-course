
# del statement
"""
motorcycles = ["Lamborghini", "Tesla", "Wolkswagen"]
print(motorcycles)

del motorcycles[-1]
print(motorcycles)
"""
# pop() method
"""
motorcycles = ["Lamborghini", "Tesla", "Wolkswagen"]

popped_motorcycle = motorcycles.pop(0)

print(motorcycles)
print(popped_motorcycle)

"""
# When you don't know the position of the item,
# you can use the remove() method

motorcycles = ["Lamborghini", "Tesla", "Wolkswagen"]
print(motorcycles)
too_expensive = "Lamborghini"
motorcycles.remove("Lamborghini")
print(motorcycles)
print(f"{too_expensive} is too expensive to me, I am poor.")
# The remove() method deletes only the first occurrence of the value
