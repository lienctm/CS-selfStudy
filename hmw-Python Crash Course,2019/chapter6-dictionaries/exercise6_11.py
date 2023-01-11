# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in,
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the infor- mation you have stored about it.

cities = {
    'Hanoi': {'country': 'Vietnam', 'population': 8418883},
    'Haiduong': {'country': 'Vietnam', 'population': 1932090},
    'Hochiminh': {'country': 'Vietnam', 'population': 9411805}
}
for city_name, city_info in cities.items():
    print(f'\n{city_name}:')
    country = city_info['country']
    population = city_info['population']
    print(f'\tcountry: {country}')
    print(f'\tpopulation: {population}')
    