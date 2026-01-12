prompt = "Digite o ingrediente que deseja, ou digite 'quit' caso já tenha "
prompt += "adicionado todos: "
added_toppings = []

while True:
    requested_topping = input(prompt)
    if requested_topping != 'quit':
        print(f"Adicionando {requested_topping}")
        added_toppings.append(requested_topping)
    else:
        print("Sua pizza será feita com os seguintes ingredientes: ")
        for topping in added_toppings:
            print(topping)
        break