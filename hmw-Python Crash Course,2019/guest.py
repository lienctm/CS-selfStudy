# a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt.
names = input("Enter your name: ")
#print("Your name is " + names)
print(f"Your name is {names}")

filename = 'guest.text'
with open(filename, 'w') as file:
    file.write(f"{names}")