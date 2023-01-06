# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping function, lstrip(), rstrip(), strip()

name = "  Micky Mouse "

print(f'The origin name: "{name}"')
print(f'The name after removed the left whitespace: "{name.lstrip()}"')
print(f'The name after removed the right whitespace: "{name.rstrip()}"')
print(f'The name after removed both side of the name: "{name.strip()}"')