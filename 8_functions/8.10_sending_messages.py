def send_messages(pending_messages, sent_messages):
    """Simula o envio de mensagens de e-mail"""
    pending_messages.reverse()
    while pending_messages:
        message = pending_messages.pop()
        print(f'Enviando mensagem com o título: {message}')
        sent_messages.append(message)

pending_messages = [
    'Confirmação de conta XPTO',
    'Reset de senha da conta ACME',
    'Promoção disponível até fevereiro'
]
sent_messages = []

send_messages(pending_messages, sent_messages)

print(f'\n{pending_messages}')
print(sent_messages)