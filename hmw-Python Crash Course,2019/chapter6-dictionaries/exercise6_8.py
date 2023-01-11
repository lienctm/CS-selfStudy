# Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.

pet1 = { "pet_name":"cat", "owner":"Kin" }
pet2 = { "pet_name":"dog", "owner":"Zuck" }
pet3 = { "pet_name":"parrot", "owner":"Bun" }
animals = [ pet1, pet2, pet3]
for animal in animals:
    print(f"{animal['owner']} has a {animal['pet_name']}")
      