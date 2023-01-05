# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
def make_shirt(size="large", message="I love Python"):
    print(f'The shirt is size {size} and printed "{message}"')

# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
make_shirt(size="medium")
make_shirt(size="unisex", message="We are together")
