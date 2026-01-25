def build_profile(first_name, last_name, **user_info):
    """Gera um dicionario contendo as informações do usuário"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name

    return user_info

new_user = build_profile('felipe', 'santos', age=23, location='São Paulo', 
                        favorite_song='A place for my head - Linkin Park')

print(new_user)