def build_profile(first_name, last_name, **user_info):
    # **user_info cause Python to create an empty dictionary called user_info
    # and pack whatever name-value pairs it receives into this dictionary
    """Build a dictionary to contain everything about user"""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('demi', 'cao',age= '20', city='haiduong', country= 'vietnam',)
print(user_profile)

def make_car(manufacture, model, **cars_info):
    cars_info['manufacture'] = manufacture
    cars_info['model'] = model
    return cars_info
cars_profile = make_car('Toyota', 'AZ2020', color= 'red', compacity ='7 seats')
print(cars_profile)

