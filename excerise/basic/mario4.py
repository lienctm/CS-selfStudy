# Write programs to print following patterns :
#    1
#   212
#  32123
# 4321234

height = 8

for row in range(height):
    for space in range(height - row - 1):
        print(" ", end="")
    for num1 in range(row + 1):
        print(row + 1 - num1, end="")
    for num2 in range(row):
        print(num2 +2, end="")
    print()