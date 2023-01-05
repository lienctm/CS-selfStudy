# Write a function find_max that accepts three numbers as arguments and returns the largest number among three.
# Write another function main, in main() function accept three numbers from user and call find_max.

def max(num1, num2, num3):
    max = 0
    if num1 >= num2 or num1 >= num3:
        max = num1
    elif num2 >= num1 or num2 >= num3:
        max = num2
    else:
        max = num3
    return max

print(max(8, 10, 2))
