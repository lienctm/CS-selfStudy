filename = 'pi_digits.txt'

with open( filename ) as file:
    lines = file.readlines()

pi_string = ' '
for line in lines:
    # Add each line in pi_digits.txt to pi_string
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))