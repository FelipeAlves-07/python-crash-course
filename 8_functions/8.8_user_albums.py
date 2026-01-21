def make_album(artist_name,album_name,number_of_songs=None):
    """Gera um dicionário com as informações recebidas sobre o album"""
    album = {'artist': artist_name, 'album': album_name}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album

user_albums = []

while True:
    print('\nPrecisamos das informações sobre o album!')
    print('Digite "q" a qualquer momento para parar a execução!\n')

    artist = input('Digite o nome do artista: ')
    if artist == 'q':
        break

    album = input('Digite o nome do album: ')
    if album == 'q':
        break

    new_album = make_album(artist, album)
    user_albums.append(new_album)

    repeat = input('Deseja registrar um novo album? (s/n): ')
    if repeat == 'n':
        break

print('Os seguintes albums foram registrados!')
print(user_albums)