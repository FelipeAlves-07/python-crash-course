word_definitions = {
    'constant': 'Variável com valor fixo durante toda a execução do programa.',
    'tupple': 'Lista que armazena valores imutáveis.',
    'list': 'Tipo de dado que armazena múltiplos itens em ordem.',
    'logical error': 'O programa é executado mas não retorna o valor esperado',
    'dict': 'Tipo de dado que armazena múltiplos itens em formato chave: valor'
    }

print('Abaixo estão as definições de alguns termos usados em programação')

word = "constant"
print(f"\n{word.title()}: {word_definitions[word]}")

word = "dict"
print(f"{word.title()}: {word_definitions[word]}")

word = "list"
print(f"{word.title()}: {word_definitions[word]}")

word = "logical error"
print(f"{word.title()}: {word_definitions[word]}")

word = "tupple"
print(f"{word.title()}: {word_definitions[word]}")