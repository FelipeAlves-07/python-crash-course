def make_shirt(size, message):
    """Faz uma camiseta com o tamanho e mensagem especificados"""
    print(f'\nFaremos uma camisa com as seguintes especificações: ')
    print(f'Tamanho: {size.upper()}')
    print(f'Mensagem: {message.capitalize()}')

make_shirt('p', 'Viva la vida')

make_shirt(message='Viva la vida', size='g')