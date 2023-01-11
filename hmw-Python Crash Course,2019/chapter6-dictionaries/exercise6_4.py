# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) 
# by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.
dicts = {
    "immutable":"the values cannot change",
    "list comprehension":"generate the same list in just one line of code",
    "index":"the position of the item",
    "comments":"Comments are code lines that will not be executed",
    "indentation":"Indentation refers to the spaces at the beginning of a code line"
}
for key, value in dicts.items():
    print(f"{key}: {value}")

# Add terms in dicts
dicts["dictionary"] = "A dictionary is an unordered, and changeable, collection"
dicts["slice"] = "How to slice a string"
for key, value in dicts.items():
    print(f"{key}: {value}")


