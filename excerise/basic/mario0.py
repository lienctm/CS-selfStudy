# Write programs to print following patterns :
# *
# * *
# * * *
# * * * *

height = 4

for row in range(height):
    print((row+1) * "* ")

#    for column in range(row+1):
#        print("*", end=" ")
#    print()

