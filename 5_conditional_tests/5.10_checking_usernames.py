current_users = ["Eduardo", "Felipe", "RENAN", "Danilo", "kauan"]
new_users = ["FELIPE", "andre", "danilo", "guilherme", "matheus"]

current_users_lowercase = [user.lower() for user in current_users]

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users_lowercase:
            print(f"Nome de usuário {new_user} já está em uso")
        else:
            print(f"Nome de usuário {new_user} disponível")
else:
    print("Nenhum usuário a ser criado")