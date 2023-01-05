# Write a function that stores information about a car in a diction- ary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the func- tion with the required information and two other name-value pairs, such as a color or an optional feature

def make_car(manufacturer, model, **info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info

car = make_car('Honda', '2020', color='white', price='$35000')
print(car)