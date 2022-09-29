# passing information to a function
def describe_city(city, country='vietnam'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('ho chi minh')
print()

# 
def build_city_country(city, country):
    city_country = f"{city}, {country}"
    return city_country.title()
name = build_city_country('hanoi', 'vietnam')
print(name)
