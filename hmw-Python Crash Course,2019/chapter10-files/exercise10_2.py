# You can use the replace() method to replace any word in a string with a different word
# Read in each line from the file you just created, learning_python.txt, and replace the word Python
# with the name of another language, such as C. Print each modified line to the screen

learningfile = 'learning_python.txt'
with open(learningfile) as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("Python", "C++")
        print(line.rstrip())
