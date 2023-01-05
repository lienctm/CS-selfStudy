# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
def make_shirt(size, message):
    print(f'The shirt is size {size} and printed "{message}"')

# Call the function once using positional arguments to make a shirt.
make_shirt("7", "Big brother")

# Call the function a second time using keyword arguments.
make_shirt(size= "7", message= "Big brother")

