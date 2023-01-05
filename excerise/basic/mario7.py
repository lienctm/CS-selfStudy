# Write programs to print following patterns :
# * * * *
# * * *
# * * 
# * 

height = 4

for row in range(height):
    for col in range(height - row):
        print("*", end=" ")
    print()