def describe_city(city, country='brasil'):
    """Gera uma string descrevendo qual é o país da cidade"""
    print(f'\n{city.title()} fica no país: {country.title()}')

describe_city('caraguatatuba')
describe_city(city='goias')
describe_city('toronto', 'canada')