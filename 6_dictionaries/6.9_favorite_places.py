favorite_places = {
    'renan': ['floresta amazonica', 'pantanal', 'sorocaba'],
    'everton': ['canto do buriti', 'osasco', 'paraiba'],
    'felipe': ['igarata', 'goiania', 'mexico'],
}

for name, places in favorite_places.items():
    print(f"\nOs locais favoritos de {name.title()} são:")
    for place in places:
        print(place.title())