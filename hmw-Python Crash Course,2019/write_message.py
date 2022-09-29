# Writing to an empty file
filename = 'programming.txt'

with open(filename, 'w') as file :
    file.write("I love programming.\n")
    file.write("I love making game.\n")

# Add more content without erase the pevious content in file, using append mode.
# with open(filename, 'a') as file :
#   file.write("I also love creating apps.")