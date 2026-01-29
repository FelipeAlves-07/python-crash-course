class User:
    """A simple attempt to represent an user."""

    def __init__(self, first_name, last_name, age, location=''):
        """Initialize attributes about an user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location


    def describe_user(self):
        """Show available user information"""
        print(f'Primeiro nome: {self.first_name.title()}')
        print(f'Último nome: {self.last_name.title()}')
        print(f'Idade: {self.age}')

        if self.location:
            print(f'Localidade: {self.location.title()}')


    def greet_user(self):
        """Show a greeting message for the user"""
        full_name = f'{self.first_name} {self.last_name}'
        print(f'Olá {full_name.title()}')

users = [
    User('felipe', 'santos', 23),
    User('lucas', 'albertini', 23),
    User('matheus', 'medeiros', 23, 'são paulo')
]

for user in users:
    user.describe_user()
    user.greet_user()
    print()