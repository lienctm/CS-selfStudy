# Write a Python program that accepts a string from user. 
# Your program should create a new string by shifting some positions to left.
# For example if the user enters the string 'examination 2021' then new string would be 'xamination 2021e'

user_input = input("Enter your text: ")
new_string = user_input[1:] + user_input[0]
print("New string after shifting 1 position is: " + new_string)

