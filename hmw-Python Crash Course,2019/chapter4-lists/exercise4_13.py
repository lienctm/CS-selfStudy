# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
foods = ("bread", "beef", "pizza", "mochi", "salad")
print("The origin menu:")
for food in foods:
    print(food)

# • Try to modify one of the items, and make sure that Python rejects the change.
# foods[0] = "sea food"

# • The restaurant changes its menu, replacing two of the items with different foods. 
# Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ("sea food", "beef", "tacos", "mochi", "salad") 
print("The revised menu:")
for food in foods:
    print(food)


