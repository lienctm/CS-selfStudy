# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sand- wich that’s being ordered. Call the function three times,
# using a different num- ber of arguments each time.

def order_sandwich(*items):
    """Build an emtpy tuple containing everything we know about a user."""
    print(items)

order_sandwich("chicken")
order_sandwich("beef and onion", "tuna and green pepper")
order_sandwich("beef", "maccaroni", "pork")