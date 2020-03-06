def city_country(city, country, population=''):
    """Zwraca sformatowany tekst zawierający miasto i kraj"""
    if population:
        city_country_r = city + ', ' + country + ' - populacja: ' + str(population)
    else:
        city_country_r = city + ', ' + country
    return city_country_r.title()
