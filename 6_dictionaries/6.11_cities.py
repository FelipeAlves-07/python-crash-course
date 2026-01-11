cities = {
    'goiania': {
        'country': 'brasil',
        'population': 1_503_256,
        'turistic_point': 'parque flamboyant',
    },
    'sorocaba': {
        'country': 'brasil',
        'population': 762_172,
        'turistic_point': 'parque zoológico municipal quinzinho de barros',
    },
    'campinas': {
        'country': 'brasil',
        'population': 1_187_974,
        'turistic_point': 'parque portugal',
    }
}

for city, city_info in cities.items():
    print(f"\nInformações disponíveis de {city.title()}:")
    country = city_info['country']
    population = city_info['population']
    turistic_point = city_info['turistic_point']

    print(f'País: {country.title()}')
    print(f'População: {population}')
    print(f'Ponto turístico mais famoso: {turistic_point.title()}')