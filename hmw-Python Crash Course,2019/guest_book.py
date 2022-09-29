# Prompt for user name. When they enter their name, print a greeting to the screen
# and add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

names = input("Enter your name: ")
print(f"Hello {names}. Welcome to the Bookshop.")

filename = 'guest_book.txt'
with open(filename,'a+') as file:
    file.write(f"{names}")


