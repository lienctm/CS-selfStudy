# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same, 
# but each message should be personalized with the person’s name.

names = ["An", "Hoa", "Binh", "Huong", "Minh"]

for i in range(len(names)):
    print(f"{names[i]} is one of my best friends.")