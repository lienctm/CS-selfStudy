# One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
# When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. 
# Add them together and print the result. Catch the ValueError if either input value is not a number,
# and print a friendly error message. Test your program by entering two numbers 
# and then by entering some text instead of a number.

print("Enter 2 numbers and I will add them together for you")
try:
    first_numer = input("\nEnter 1st number: ")
    second_number = input("Enter 2nd number: ")
except ValueError:
    print("It is not a number")
else:
    add_number = f'{first_numer}{second_number}'
    print(add_number)


