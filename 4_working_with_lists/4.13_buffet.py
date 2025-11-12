menu = ("x-salada", "x-burguer", "x-bacon", "fritas", "nuggets")

print("Os itens disponíveis no cardápio são os seguintes:")
for food in menu:
    print(f"\t- {food}")

# A linha abaixo irá gerar um erro, ela foi utilizada apenas para validar a Tuple, por isso está comentada.
#menu[0] = "x-egg"

menu = ("x-burguer", "x-egg", "hot dog", "fritas", "onion rings")

print("\nO cardápio sofreu alterações, os itens disponíveis são:")
for food in menu:
    print(f"\t- {food}")