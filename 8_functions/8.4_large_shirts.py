def make_shirt(size='g', message='i love Python'):
    """Faz uma camiseta com o tamanho e mensagem especificados"""
    print(f'\nFaremos uma camisa com as seguintes especificações: ')
    print(f'Tamanho: {size.upper()}')
    print(f'Mensagem: {message.capitalize()}')

make_shirt()

make_shirt(size='m')

make_shirt('gg', 'Viva la vida')