# Write a program that accepts a string from user. 
# Your program should count and display number of vowels in that string

text = input("Enter your text: ")
    
count = 0
for character in text:
    if character in 'aeiouAEIOU':
        count = count + 1
print(f"Your text has {count} vowels.")



