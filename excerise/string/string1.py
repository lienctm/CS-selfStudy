# Write a program that reads a string from keyboard and display:
# The number of uppercase letters in the string
# The number of lowercase letters in the string
# The number of digits in the string
# The number of whitespace characters in the string

user_input = input("Enter your text: ")

upperLetters = lowerLetters = digits = whitespace = 0
for character in user_input:
    if character.isupper():
        upperLetters += 1
    elif character.islower():
        lowerLetters += 1
    elif character.isdigit():
        digits += 1
    elif character == " ":
        whitespace += 1
    
print(f"The number of uppercase letters in the string is: {upperLetters}")
print(f"The number of lowercase letters in the string is: {lowerLetters}")
print(f"The number of digits in the string is: {digits}")
print(f"The number of whitespace character in the string is: {whitespace}")
