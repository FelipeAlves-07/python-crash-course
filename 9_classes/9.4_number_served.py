class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Define the attributes that describes a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Show all available information about the restaurant"""
        print(f'Nome do restaurante: {self.restaurant_name}')
        print(f'Tipo de culinária: {self.cuisine_type}')


    def open_restaurant(self):
        """Show a message informing the restaurant is open"""
        print(f'Restaurante {self.restaurant_name} está aberto!')


    def show_number_served(self):
        """Show the number of customers that has been served"""
        response = f'O restaurante {self.restaurant_name} já serviu '
        response += f'{self.number_served} clientes'

        print(response)


    def set_number_served(self, served_customers):
        """Update the number of served customers"""
        if served_customers >= self.number_served:
            self.number_served = served_customers
        else:
            print('O número de clientes servidos não pode ser diminuido!')

    def increment_number_served(self, served_customers):
        """Increment served customer's number with the value passed"""
        if served_customers >= 0:
            self.number_served += served_customers
        else:
            print('O número de clientes servidos não pode ser diminuido!')

restaurant = Restaurant('Fogo de Chão', 'Brasileira')

restaurant.show_number_served()
restaurant.number_served = 10
restaurant.show_number_served()

restaurant.set_number_served(20)
restaurant.show_number_served()

restaurant.increment_number_served(15)
restaurant.show_number_served()
