# count the consecutive element

list = [ 4, 5, 5, 5, 6, 7, 7, 8, 9, 0, 0, 0]

sub_list = []

print(len(list))
# getting the consecutive element
for index in range(len(list)):
    if list[index] == list[index + 1]:
        sub_list.append(list[index])

count_sub_list = len(list(set(sub_list)))
print(count_sub_list)