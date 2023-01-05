# factorial of a number is follows: n! = n * (n-1)!

def factorial_recursive(n):
    # base case:
    if n == 1:
        return 1
    # recursive case:
    else:
       return n * factorial_recursive(n-1)
    
user_input = input("Enter a number: ")
factorial_number = factorial_recursive(int(user_input))
print(f"Factorial of {user_input} is {factorial_number}")
