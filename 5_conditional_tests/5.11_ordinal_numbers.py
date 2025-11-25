numbers = [value for value in range(1,10)]

if numbers:
    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number > 2 and number < 10:
            print(f"{number}th")
else:
    print("Lista de números vazia!")