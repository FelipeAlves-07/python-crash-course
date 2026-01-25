def register_car(manufacturer, model, **car_info):
    """Gera um dicionario contendo informações do carro especificado"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

new_car = register_car('honda', 'civic', color='black', year=2008)
print(new_car)