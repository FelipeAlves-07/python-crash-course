requested_car = ""
prompt = "Digite o modelo do carro que você gostaria de alugar: "

while not requested_car:
    requested_car = input(prompt)
    
print(f"Vamos verificar se algum {requested_car} está disponível!")