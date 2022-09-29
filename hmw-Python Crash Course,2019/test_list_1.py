nums = [1, 3, 10, 40, 50]
min = min(nums)
print(f"Minimum number is: {min}")

max = max(nums)
print(f"Maximum number is: {max}")

odd_nums = list(range(1,20,2))
print(odd_nums)
# a list comprehension
list = [ value * 3 for value in range(1,11)]
print(list)
# a list comprehension
cube = [ value ** 3 for value in range(1, 10)]
print(cube)

cube_1 = []
for value in range(1,10):
    #cube = value ** 3
    #cube_1.append(cube)
    cube_1.append(value ** 3)
print(cube_1)

