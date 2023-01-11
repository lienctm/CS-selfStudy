# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output.
dicts = {
    "immutable":"the values cannot change",
    "list comprehension":"generate the same list in just one line of code",
    "index":"the position of the item",
    "comments":"Comments are code lines that will not be executed",
    "indentation":"Indentation refers to the spaces at the beginning of a code line"
}
for word in dicts:
    print(f"{word}: {dicts[word]}")