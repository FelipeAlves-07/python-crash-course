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

restaurants = [
    Restaurant('Fogo de Chão', 'Brasileira'),
    Restaurant('Si Señor', 'Mexicana'),
    Restaurant('Matsuya', 'Japonesa'),
]

for restaurant in restaurants:
    restaurant.describe_restaurant()
    print()