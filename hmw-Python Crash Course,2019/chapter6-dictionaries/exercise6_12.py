# We’re now working with examples that are complex enough that they can be extended in any number of ways. 
# Use one of the example pro- grams from this chapter, and extend it by adding new keys and values,
# chang- ing the context of the program or improving the formatting of the output.
people = {
    "An":1,
    "Nhi":15,
    "Luna":8,
    "Ken": 20,
    "Bun":99
}

# change value
people["An"] = 10
# add new keys and values
people["Chica"] = 100
people["Bibo"] = 45

for k, v in people.items():
    print(f'{k}: {v}')

