#the append() method adds an item to the end of the list
num = [ 10, 20, 30, 40]
num.append(50)
#equivalent to num.append(50)
#num.inset(4,50)
#num[len(num):] = [50]
print(num)

a = [60, 70, 80]
b = (90, 100)  
a.append(b)   #append() adds only a single item at a time
print(a)

a.extend(b)   #extend() adds many items
print(a)
