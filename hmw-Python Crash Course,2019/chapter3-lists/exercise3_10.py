# Think of something you could store in a list. For example, you could make a list of mountains, 
# rivers, countries, cities, languages, or any- thing else you’d like. Write a program that 
# creates a list containing these items and then uses each function introduced in this chapter at least once.

favorite_food = []

favorite_food.append("pho")
favorite_food.insert(0,"spring roll")
favorite_food.insert(1,"banh xeo")
favorite_food.append("mochi")
print(f"favorite food list: {favorite_food}")
print(f"Length of the list: {len(favorite_food)}")

favorite_food.sort()
print(f"The sorted list: {favorite_food}")

favorite_food.reverse()
print(f"Reversed list: {favorite_food}")

favorite_food.pop(3)
print(f"The list after pop out 'banh xeo': {favorite_food}")

favorite_food.remove("spring roll")
print(f"The list after removed 'spring roll': {favorite_food}")

del favorite_food[1]
print(f"The final list: {favorite_food}")




