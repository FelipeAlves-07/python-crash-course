people_count = input('Digite a quantidade de pessoas: ')
people_count = int(people_count)

if people_count < 8:
    print("Temos uma mesa disponível, entrem!")
elif people_count <= 20:
    message = f"Não temos nenhuma mesa disponível no momento para "
    message += f"{people_count} pessoas, aguardem!"
    print(message)
else:
    print("A quantidade máxima é de 20 pessoas por mesa!")