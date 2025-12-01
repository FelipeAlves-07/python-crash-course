word_definitions = {
    'constant': 'Variável com valor fixo durante toda a execução do programa.',
    'tupple': 'Lista que armazena valores imutáveis.',
    'list': 'Tipo de dado que armazena múltiplos itens em ordem.',
    'logical_error': 'O programa é executado mas não retorna o valor esperado',
    'dict': 'Tipo de dado que armazena múltiplos itens em formato chave: valor',
    'set': 'Conjunto de dados de valores únicos',
    
    }

print('Abaixo estão as definições de alguns termos usados em programação\n')

for word, definition in sorted(word_definitions.items()):
    if "_" in word:
        word = word.replace("_", " ")
    print(f"{word.title()}: {definition}")