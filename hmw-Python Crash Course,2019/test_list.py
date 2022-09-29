motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
#add item to the end of the list
motocycles.append('ducati')
print(motocycles)

#add item at any position in the list
motocycles.insert(0,'misubishi')
print(motocycles)

#remove element from the list, not use it anymore
del motocycles[1]
print(motocycles)

#remove the last item in the list, use it as removed from the list
popped_motocycles = motocycles.pop()
print(popped_motocycles)

#remove an item by value, don't know the position
motocycles.remove('yamaha')
print(motocycles)