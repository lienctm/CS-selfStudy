# Write a function that takes in two numbers and
# recursively multiplies them together.

def multiplies_recursive(num1, num2):
    if num2 == 1:
        return num1 * num2
    else:
        return num1 + multiplies_recursive(num1, num2 - 1)

num1 = 4
num2 = 10
print(multiplies_recursive(num1, num2))