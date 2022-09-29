lists = [ 'haiduong', 'banhdauxanh', 'gamai', 'tauhoa', 'nhacaotang']
for list in lists :
    if list == 'tauhoa':
        print(list.upper())
    else :
        print(list.title())

list_1 = 'huong'
if list_1 not in lists:
    print(f"{list_1} is not in the list")