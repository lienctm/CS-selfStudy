# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# Expected output is 55

def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)
    
user_input = input("Chosse your number from 1 to 10: ")
value = sum_recursive(int(user_input))
print(f"Sum of numbers from 0 to {user_input} is {value} ")
