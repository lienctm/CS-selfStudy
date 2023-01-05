# Write programs to print following patterns :
# 1
# 1 2
# 1 2 3
# 1 2 3 4

height = 4

for row in range(height):
    for column in range(row+1):
        print(column + 1, end=" ")
    print()