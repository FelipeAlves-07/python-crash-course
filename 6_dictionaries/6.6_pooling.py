favorite_languages = {
    'felipe': 'python',
    'lucas': 'c#',
    'derek': 'python',
    'fabio': 'go'
    }

pending_people = ['lucas', 'pedro', 'derek', 'victoria']

for person in pending_people:
    print(f"Olá {person.title()}")
    if person in favorite_languages:
        print("\tVocê já respondeu a pesquisa! Obrigado.")
    else:
        print("\tPesquisa sem resposta, deseja responder agora?")