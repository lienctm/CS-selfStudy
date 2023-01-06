# Write a while loop that prompts users for their name. When they enter their name,
# print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

while True:
    names = input("Enter your name: ")
    if names != "":
        print(f"Hello {names}. Welcome to the Bookshop.")
        filename = 'guest_book.txt'
        with open(filename,'a') as file:
            file.write(f"{names}\n")
    else:
        break

