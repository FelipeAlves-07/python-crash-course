import random

start_game = True

while start_game:
    number = random.randint(1, 50)
    guess = int(input("Estou pensando em um número, tente adivinha-lo: "))

    while not guess == number:
        if guess < number:
            guess = int(input("Muito Baixo! Tente novamente: "))
        if guess > number:
            guess = int(input("Muito Alto! Tente novamente: "))

    answer = input("Correto! Deseja jogar novamente? (sim/nao)").upper()
    if answer == "NAO":
        print("Obrigado por jogar! :)")
        start_game = False
