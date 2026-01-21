def city_country(city, country):
    """Gera uma string no formato 'Cidade, País'"""
    response = (f'"{city.title()}, {country.title()}"')
    return response

cities = {'amazonas': 'brasil', 'toronto': 'canada', 'kyoto': 'japão'}

for city, country in cities.items():
    formatted_city = city_country(city, country)
    print(formatted_city)
