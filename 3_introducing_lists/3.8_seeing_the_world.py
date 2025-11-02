places = [
    "florianopolis",
    "mexico",
    "grecia",
    "salvador",
    "japao"
]

# Manipulando a ordem da lista temporariamente
print(f"Lista Original:\n{places}")

print(f"\nLista Ordenada:\n{sorted(places)}")

print(f"\nLista Original:\n{places}")

print(f"\nLista Ordenada de trás para frente:\n{sorted(places, reverse=True)}")

print(f"\nLista Original:\n{places}")


# Manipulando a ordem da lista permanentemente
places.reverse()
print(f"\nLista em ordem reversa:\n{places}")

places.reverse()
print(f"\nLista Original:\n{places}")

places.sort()
print(f"\nLista Ordenada:\n{places}")
print(f"\nLista Original:\n{places}")

places.sort(reverse=True)
print(f"\nLista Ordenada de trás para frente:\n{sorted(places, reverse=True)}")
print(f"\nLista Original:\n{places}")