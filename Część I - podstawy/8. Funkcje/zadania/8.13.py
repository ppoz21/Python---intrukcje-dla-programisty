def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie ifnormacje
    o użytkowniku"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('janusz', 'nosacz',
                             location='białystok',
                             job='bezrobotny',
                             intrested_in='wódka',
                             relationship='grażyna')
print(user_profile)
