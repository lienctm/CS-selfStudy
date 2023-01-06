# Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file.
# Write a separate pro- gram that reads in this value and prints the message, “I know your favorite number! It’s _____.”

import json

favorite_number = input("Enter your a favorite number: ")
filename = 'favorite_number.json'
with open(filename, 'w') as file:
    json.dump(favorite_number, file)

with open(filename) as f:
    number = json.load(f)
    print(f"Your favorite number is {number}")
