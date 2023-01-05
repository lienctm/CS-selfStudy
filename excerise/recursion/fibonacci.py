# Fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13,…

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = 4
for i in range(num):
    print(fibonacci(i), end=" ")
print()