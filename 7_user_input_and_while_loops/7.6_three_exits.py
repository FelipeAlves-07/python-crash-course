active = True

while active:
    person_age = input('Digite sua idade, ou digite "quit" para finalizar: ')
    if person_age == 'quit':
        break

    person_age = int(person_age)
    if person_age < 3:
        ticket_price = 0
    elif person_age <= 12:
        ticket_price = 10
    elif person_age <= 122:
        ticket_price = 15
    else:
        print("Idade inválida!")
        active = False
        continue

    message = f'Seu ingresso custará R$ {ticket_price}'
    print(message)