
# When you want to do the same action with every item in a list,
# you can use Python's for loop.

"""
z_warriors = ["Goku", "Vegeta", "Picollo", "Gohan", "Krillin"]
for warrior in z_warriors:
    print(warrior)

    """
# We should read it like this:
# For every warrior in the list of z-warriors, print the warrior's name.
# It is helpful to choose a meaningful name for the temporary variable.
# For example:  for cat in cats: , for dog in dogs:

z_warriors = ["Goku", "Vegeta", "Picollo", "Gohan", "Krillin"]

for warrior in z_warriors:
    print(f"Dear z warrior {warrior}, thanks for saving the Universe")
    print(f"That was an outstanding participation, z warrior {warrior}\n")
