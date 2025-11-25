# Cópia do exercício 5.8, exibindo as mensagens apenas se a lista 
# usernames não estiver vazia
usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Olá {username}, gostaria de ver o status da plataforma?")
        else:
            print(f"Olá {username}, bem vindo de volta!")
else:
    print("Nenhum usuário encontrado!")