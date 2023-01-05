# Write a Python program that accepts a string from user.
# Your program should create a new string in reverse of first string and display it

user_input = input("Origin text: ")
new_string = user_input[::-1]
print(f"Reversed text: {new_string}") 