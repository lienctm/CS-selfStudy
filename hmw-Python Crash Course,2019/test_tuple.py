
members = [
    ("Dad",1987), ("Mom",1990), ("Daughter",2018), ("Son",2021)
]

for mem, year in members:
    #format() formats the specified value and insert them inside the string's placeholder {}
    print ( "{} was born in {}".format(mem, year))