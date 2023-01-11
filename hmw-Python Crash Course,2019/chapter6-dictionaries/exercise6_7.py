# Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people,
#  and store all three dictionaries in a list called people. Loop through your list of people.
#  As you loop through the list, print everything you know about each person.

person1 = { "firstName":"Blanca", "lastName":"Bolton", "age":60, "city":"Santa Barbara" }
person2 = { "firstName":"Bob", "lastName":"Hilton", "age":45, "city":"San Diego" }
person3 = { "firstName":"Kim", "lastName":"Wake", "age":20, "city":"San Francisco" }
people = [ person1, person2, person3]
for person in people:
    full_name = person["firstName"] + " " + person["lastName"]
    print(full_name)
    print(f"age: {person['age']},")
    print(f"city: {person['city']},\n")