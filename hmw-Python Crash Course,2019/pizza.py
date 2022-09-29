# PASSING AN ARBITRARY NUMBER OF ARGUMENTS

def make_pizza(*toppings):
    # make an empty tuple called toppings and pack whatever values it receives into this tuple.
    
    #print("\nMaking a pizza with the folowing toppings:")
    #for topping in toppings:
     #   print(f"- {toppings}")
    print(toppings)

make_pizza('peperroni', 'mushroom', 'chicken', 'green pepper')
make_pizza('extra cheese')


# Note: neeed to recheck! The result is not same in the book.