# Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers
# even if they make a mistake and enter text instead of a number.
print("Enter 2 numbers and I will add them together for you")
while True:
    first_numer = input("\nEnter 1st number: ")
    if first_numer not in '1234567890':
        print("It is not a number")
        break
    second_number = input("Enter 2nd number: ")
    if second_number not in '1234567890':
        print("It is not a number")
        break
    add_number = f'{first_numer}{second_number}'
    print(add_number)


