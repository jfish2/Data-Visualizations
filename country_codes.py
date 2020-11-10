#country_codes.py
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name == 'Egypt, Arab Rep.':
        code = 'eg'
        return code
    elif country_name == 'Bolivia':
        code = 'bo'
        return code
    elif country_name == 'Venezuela, RB':
        code = 've'
        return code
    elif country_name == 'Guyana':
        code = 'gf'
        return code
    elif country_name == 'Libya':
        code = 'ly'
        return code
    elif country_name == 'Congo, Dem. Rep.':
        code = 'cd'
        return code
    elif country_name == 'Tanzania':
        code = 'tz'
        return code
    elif country_name == 'Korea, Rep.':
        code = 'kr'
        return code


    return None
