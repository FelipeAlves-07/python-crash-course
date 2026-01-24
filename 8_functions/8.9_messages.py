def show_messages(messages):
    """Mostra cada mensagem dentro de uma lista"""
    for message in messages:
        print(message)

messages = [
    'Confirmação de conta XPTO',
    'Reset de senha banco ACME',
    'Promoção disponível até fevereiro'
]

show_messages(messages)