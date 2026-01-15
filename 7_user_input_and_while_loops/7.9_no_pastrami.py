sandwich_orders = [
    'x-burger', 'pastrami', 'x-bacon', 'pastrami', 'x-salada', 'x-tudo',
    'pastrami'
    ]
finished_sandwiches = []

print('Não temos todos os ingredientes disponíveis para o Pastrami!\n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'O {order.title()} foi feito!')
    finished_sandwiches.append(order)

print('\nOs seguintes lanches estão prontos:')
for sandwich in finished_sandwiches:
    print(sandwich.title())