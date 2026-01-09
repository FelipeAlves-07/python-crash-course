favorite_numbers = {
    'caique': [],
    'enzo': [7, 14],
    'renan': [27, 420],
    'guilherme': [5],
    'everton': [4, 24]
}

for person, numbers in favorite_numbers.items():
    if not numbers:
        print(f'{person.title()} não possui nenhum número favorito.')
        continue

    if len(numbers) > 1:
        print(f"\nOs números favoritos de {person.title()} são:")
    else:
        print(f"\nO número favorito de {person.title()} é:")
        
    for number in numbers:
        print(number)



