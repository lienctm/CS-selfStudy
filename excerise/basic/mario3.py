# Write programs to print following patterns :
# * * * * * 
#   * * *
#     * 

height = 4

for row in range(height):
    for space in range(row):
        print(" ", end=" ")
    # for star in range((height + 2) - (2 * row)):
    for star in range((2*height - 1) - (2 * row)):
        print("*", end=" ")
    print()