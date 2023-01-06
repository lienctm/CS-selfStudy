# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

names = input("Enter your name: ")
print(f"Your name is {names}")

filename = 'guest.txt'
with open(filename, 'w') as file:
    file.write(f"{names}")