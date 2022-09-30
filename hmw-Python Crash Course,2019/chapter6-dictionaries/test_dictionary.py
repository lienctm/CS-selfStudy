pizzas = {
    "cheese" : 9,
    "pepperoni" : 7,
    "chicken" : 10,
    "vegetable" : 8
}

for pie in pizzas:
    print (pie)

for pie,price in pizzas.items():
    print (price)

for pie,price in pizzas.items():
    print ("A whole {} pizza costs ${}".format(pie, price))
    # print ("A whole",pie ,"pizza cost $", str(price))