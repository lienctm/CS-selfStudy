#  Write a function called city_country() that takes in the name of a city and its country
# Call your function with at least three city-country pairs, and print the values that are returned

def city_country(city, country):
    return f"{city} is in {country}"

value1 = city_country("Hanoi", "Vietnam")
value2 = city_country("Paris", "France")
value3 = city_country("Mumbai", "India")
print(value1)
print(value2)
print(value3)

