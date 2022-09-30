learningfile = 'learning_python.txt'

# Print the file content by reading in the entire file, line by line
#with open(learningfile) as file:
#   for line in file:
#      print(line)

with open(learningfile) as file:
    lines = file.readlines()
# Print content by storing line in a list by looping over the file
#for line in lines:
#    print(line.rstrip())

# Print content by storing line in a string
py_string = ''
for line in lines:
    py_string  += line
print(py_string)


