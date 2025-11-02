# Este código tem o objetivo de usar todos os métodos e funções aprendidos para interagir com itens dentro de uma lista

languages = []
print(f"Lista inicial:\n{languages}")

new_language = "ingles"
languages.append(new_language)
print(f"\nIdioma {new_language} adicionado.\n{languages}")

new_language = "espanhol"
languages.append(new_language)
print(f"\nIdioma {new_language} adicionado.\n{languages}")

new_language = "italiano"
languages.append(new_language)
print(f"\nIdioma {new_language} adicionado.\n{languages}")

new_language = "portugues"
languages.insert(0, new_language)
print(f"\nIdioma {new_language} adicionado.\n{languages}")

print(f"\nQuantidade de idiomas: {len(languages)}")

new_language = "frances"
print(f"\nIdioma {languages[3]} substituido por {new_language}.")
languages[3] = "frances"
print(languages)


print(f"\nLista de idiomas ordenada temporariamente:\n{sorted(languages)}")


languages.reverse()
print(f"\nLista de idiomas em ordem reversa:\n{languages}")


languages.sort()
print(f"\nLista de idiomas ordenada permanentemente:\n{languages}")


print(f"\nIdioma {languages[1]} removido!")
del languages[1]
print(languages)

remove_language = "espanhol"
languages.remove(remove_language)
print(f"\nIdioma {remove_language} removido!\n{languages}")


popped_language = languages.pop()
print(f"\nIdioma {popped_language} removido da lista pois já foi aprendido!")
print(languages)

popped_language = languages.pop()
print(f"\nIdioma {popped_language} removido da lista pois já foi aprendido!")
print(languages)

print(f"\nEstado final da lista: \n{languages}")