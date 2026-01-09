person_0 = {
    'first_name': 'felipe',
    'last_name': 'santos',
    'age': 23,
    'city': 'sao paulo'
    }

person_1 = {
    'first_name': 'danilo',
    'last_name': 'bifano',
    'age': 26,
    'city': 'sorocaba'
    }

person_2 = {
    'first_name': 'luca',
    'last_name': 'barreto',
    'age': 22,
    'city': 'parana'
    }

people = [person_0, person_1, person_2]

print("Lista de pessoas:")
for person in people:
    print(f"\nPrimeiro nome: {person['first_name'].title()}")
    print(f"Último nome: {person['last_name'].title()}")
    print(f"Idade: {person['age']}")
    print(f"Cidade: {person['city'].title()}")