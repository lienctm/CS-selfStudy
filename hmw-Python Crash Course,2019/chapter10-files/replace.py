# Replace anyword in the string with a different word.
message = "I really like dog."
new_message = message.replace('dog', 'cat')
print(new_message)

filename = 'learning_python.txt'
with open(filename) as file:
    lines = file.readlines()

text = ''
for line in lines:
    text += line

new_text = text.replace('Python', 'C')
print("This is new file after change a word Python to C :")
print(new_text)


