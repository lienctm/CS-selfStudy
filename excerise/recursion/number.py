# Write a function using recursion to print numbers from n to 0.

def num_recursive(n):
    # base case:
    print(n)
    # recursive case
    if n > 0:
        num_recursive(n-1)
        

num = 5
num_recursive(num)
