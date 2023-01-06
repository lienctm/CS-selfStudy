# Write a program that reads the files you found at Project Gutenberg and determines how many times
# the word 'the' appears in each text. This will be an approximation because it will also count words
# such as 'then' and 'there'. Try counting 'the ', with a space in the string, and see how much lower your count is.

filename = 'gutenberg.txt'
line_number = 0
with open(filename, 'r') as file:
    lines =  file.readlines()
    for line in lines:
        count = line.lower().count('the')
        line_number += 1
        print(f'{line_number}: {count}')


