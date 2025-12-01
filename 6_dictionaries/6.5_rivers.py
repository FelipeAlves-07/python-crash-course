# uma sentença de cada rio, todos os rios e todos os países
rivers = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'congo': 'africa'
    }

for river, country in rivers.items():
    print(f"O rio {river.title()} corre pelo(a) {country.title()}")

print("\nLista de rios:")
for river in rivers:
    print(f"{river.title()}")

print("\nLista de países:")
for country in rivers.values():
    print(f"{country.title()}")