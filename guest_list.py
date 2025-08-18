
# 3.4 Guest List

guests = ["Schoppenhauer", "Cicero", "Marco Aurelio Denegri"]

print(
    f"Dear great thinker {guests[0]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[1]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[2]}, you've been invited to a dinner in my house.")

# 3.5 changing guest list

print(f" Unfortunately {guests[1]} can't make it")
guests[1] = "Ruben Darío"
print(guests)

print(
    f"Dear great thinker {guests[0]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[1]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[2]}, you've been invited to a dinner in my house.")

print()

print(
    f"Dear great thinker {guests[0]}, we have a bigger table, so more people will be invited.")
print(
    f"Dear great thinker {guests[1]}, we have a bigger table, so more people will be invited.")
print(
    f"Dear great thinker {guests[2]}, we have a bigger table, so more people will be invited.")

guests.insert(0, "Francesco Petrarca")
guests.insert(2, "William Shakespeare")
guests.append("Miguel de Cervantes")
print()
print(
    f"Dear great thinker {guests[0]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[1]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[2]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[3]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[4]}, you've been invited to a dinner in my house.")
print(
    f"Dear great thinker {guests[5]}, you've been invited to a dinner in my house.")

print()
print(f"""Unfortunately, {guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]}, {guests[5]}, we won't be able to receive you all, we can invite only 
      two people for dinner.""")

dario = guests.pop(3)
print(guests)
print(f"Dear {dario}, I'm afraid to inform you that due to lack of space, you won't be able to attend the dinner.")
petrarca = guests.pop(0)
print(guests)
print(f"Dear {petrarca}, I'm afraid to inform you that due to lack of space, you won't be able to attend the dinner.")
cervantes = guests.pop(3)
print(guests)
print(f"Dear {cervantes}, I'm afraid to inform you that due to lack of space, you won't be able to attend the dinner.")
shakespeare = guests.pop(1)
print(guests)
print(f"Dear {shakespeare}, I'm afraid to inform you that due to lack of space, you won't be able to attend the dinner.")
print()
print(f"Dear {guests[0]}, you are still invited")
print(f"Dear {guests[1]}, you are still invited")
print()
del guests[0:2]
print(guests)
