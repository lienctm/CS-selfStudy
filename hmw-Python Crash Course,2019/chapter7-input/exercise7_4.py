# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

toppings = "Enter your pizza toppings: "
message = ""
while message != "quit":
    message = input(toppings)
    if message != "quit":
        print(f"I will add {message} in your pizza")
    else:
        break
    