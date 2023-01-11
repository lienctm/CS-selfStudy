# Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'.
#• Use a loop to print a sentence about each river, such as The Nile runs through Egypt
docs = { "Nile": "Egypt", "Mekong":"Vietnam", "Amazon":"Peru" }
for k, v in docs.items():
    print(f"The {k} runs through {v}")

#• Use a loop to print the name of each river included in the dictionary.
for key in docs.keys():
    print(key)
    
#• Use a loop to print the name of each country included in the dictionary.
for key in docs.values():
    print(key)


