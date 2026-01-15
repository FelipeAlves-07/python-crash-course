dream_vacations = {}
place_prompt = 'Se você pudesse viajar para qualquer lugar do mundo, '
place_prompt += 'digite qual seria: '
active = True

while active:
    person_name = input('Digite o seu nome: ')
    place = input(place_prompt)
    repeat = input('Deseja registrar a viagem de outra pessoa? (sim/nao): ')

    if repeat == 'nao':
        active = False

    dream_vacations[person_name] = place

print('\nDados registrados: \n')
for person, place in dream_vacations.items():
    print(f'{person.title()} viajaria para {place.title()}')