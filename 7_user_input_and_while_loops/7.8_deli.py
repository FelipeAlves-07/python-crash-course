sandwich_orders = ['x-burger', 'x-bacon', 'x-salada', 'x-tudo']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'O {order.title()} foi feito!')
    finished_sandwiches.append(order)

print('\nOs seguintes lanches estão prontos:')
for sandwich in finished_sandwiches:
    print(sandwich.title())