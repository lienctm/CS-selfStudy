# Write programs to print following patterns :
#    1
#   222
#  33333
# 4444444

height = 7

for row in range(height):
    for space in range(height - row - 1):
        print(" ", end="")
    for num in range(2*row + 1):
        print(row + 1, end="")
    print()
