my_flavours = ["pepperoni", "calabresa", "frango e catupiri", "mussarela"]
friend_flavours = my_flavours[:]

my_flavours.append("bacon")
friend_flavours.append("marguerita")

print("Meus sabores favoritos de pizza são:")
for flavour in my_flavours:
    print(f"\t- {flavour.title()}")

print("\nOs sabores favoritos de pizza do meu amigo são:")
for flavour in friend_flavours:
    print(f"\t- {flavour.title()}")
