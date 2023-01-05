# Write a program to accept a string from the user and display characters
# that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’

str = input("Enter your word: ")
size = len(str)

print("Printing only even index character")
for index in range(0, size, 2):
    print(str[index], end=" ")
print()

print("Printing only odd index character")
for index in range(1, size, 2):
    print(str[index], end=" ")
print()

print("Printing all characters using enumerate()")
for index, character in enumerate(str):
    print(index, character)
print()

print("Printing only even character using enumerate()")
for index, character in enumerate(str):
    if index % 2 == 0:
        print(index, character)
print()
