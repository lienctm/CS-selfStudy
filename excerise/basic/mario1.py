# Write programs to print following patterns :
#       *
#     * *
#   * * *
# * * * *

height = 6

for row in range(height):
    print((height - row - 1) * '  ' + (row + 1) * '* ')
#    for space in range(height - row - 1):
#        print(" ", end=" ")
#    for star in range(row + 1):
#        print("*", end=" ")
#    print()

