def make_sandwich(*ingredients):
    """Simula o preparo de um lanche com os ingredientes solicitados!"""
    print('Faremos um lanche com os seguintes ingredientes:')
    for ingredient in ingredients:
        print(f'- {ingredient.title()}')
    print()

make_sandwich('pão', 'carne', 'queijo')

make_sandwich('pão', 'carne', 'queijo', 'alface', 'tomate')

make_sandwich('pão', 'carne', 'queijo', 'bacon')