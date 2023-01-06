# Modify your except block in Exercise 10-8 to fail silently if either file is missing

file_name = 'dogs.txt'
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line.rstrip())