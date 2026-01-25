def make_album(artist_name,album_name,number_of_songs=None):
    """Gera um dicionário com as informações recebidas sobre o album"""
    album = {'artist': artist_name, 'album': album_name}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album