# Combine the two programs from Exercise 10-11 into one file. If the number is already stored,
# report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. 
# Run the program twice to see that it works.

import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    favorite_number = input("Enter your a favorite number: ")
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
        print(f'Your favorite number is {favorite_number}')
else:
    print(f"I know your favorite number. It's {number}")
