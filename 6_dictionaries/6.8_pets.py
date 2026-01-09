pets = []

pet = {
    'kind': 'calopsita',
    'owner': 'guilherme'
    }
pets.append(pet)

pet = {
    'kind': 'gato',
    'owner': 'derek'
    }
pets.append(pet)

pet = {
    'kind': 'cachorro',
    'owner': 'enzo'
    }
pets.append(pet)

for pet in pets:
    print(f"{pet['owner'].title()} tem um(a) {pet['kind'].title()}\n")