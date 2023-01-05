# Write programs to print following patterns :
#    1
#   123
#  12345
# 1234567

height = 5

for row in range(height):
    for space in range(height - row - 1):
        print(" ", end="")
    for num in range(2*row + 1):
        print(num + 1, end="")
    print()
