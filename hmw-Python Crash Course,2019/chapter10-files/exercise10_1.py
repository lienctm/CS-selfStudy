# Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. 
# Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt 
# in the same directory as your exercises from this chapter.
# Write a program that reads the file and prints what you wrote three times. 
# Print the contents once by reading in the entire file, once by looping over the file object,
# and once by stor- ing the lines in a list and then working with them outside the with block

learningfile = 'learning_python.txt'
with open(learningfile) as file:
    #print("Print the contents once by reading the entire file:")
    #lines = file.read()
    #print(lines)

    #print("\nPrint the contents once by looping over the file object:")
    #for line in file:
    #    print(line.rstrip())

    print("\nPrint the contents once by storing line in a list:") 
    lines = file.readlines()
    for line in lines:
        print(line.rstrip())
