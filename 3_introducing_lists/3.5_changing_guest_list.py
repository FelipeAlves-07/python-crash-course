guests = [
    "guilherme",
    "matheus",
    "lucas"
]
invitation_message = "estou organizando um jantar para o próximo sábado as 20h, e estou enviando essa mensagem como convite. Nos vemos lá!"

print(f"Olá {guests[0].title()}, {invitation_message}")
print(f"Olá {guests[1].title()}, {invitation_message}")
print(f"Olá {guests[2].title()}, {invitation_message}")

print(f"\nInfelizmente {guests[2].title()} não poderá comparecer.\n")

# Substituição do convidado indisponível
guests[2] = "everton"

print(f"Olá {guests[0].title()}, {invitation_message}")
print(f"Olá {guests[1].title()}, {invitation_message}")
print(f"Olá {guests[2].title()}, {invitation_message}")