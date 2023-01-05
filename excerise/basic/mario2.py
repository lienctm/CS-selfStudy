# Write programs to print following patterns :
#     * 
#   * * *
# * * * * *

height = 4

for row in range(height):
     print((height - row - 1) * '  ' + (2 * row + 1) * '* ')
#    for space in range(height - row - 1):
#        print(" ", end=" ")
#    for star in range(row * 2 + 1):
#       print("*", end=" ")
#    print()