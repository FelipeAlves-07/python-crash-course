class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Define the attributes that describes a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Show all available information about the restaurant"""
        print(f'Nome do restaurante: {self.restaurant_name}')
        print(f'Tipo de culinária: {self.cuisine_type}')


    def open_restaurant(self):
        """Show a message informing the restaurant is open"""
        print(f'Restaurante {self.restaurant_name} está aberto!')


restaurant = Restaurant('Fogo de Chão', 'Brasileira')

print(f'Informações retornadas manualmente: ')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print('\nInformações retornadas usando o método describe_restaurant')
restaurant.describe_restaurant()

restaurant.open_restaurant()