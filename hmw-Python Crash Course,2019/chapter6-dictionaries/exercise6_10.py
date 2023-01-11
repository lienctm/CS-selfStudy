# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number.
# Then print each per- son’s name along with their favorite numbers.
people = {
    "An": [1, 38],
    "Nhi": [15, 25, 59, 86],
    "Luna": [8, 10],
    "Ken": [20, 45, 66],
    "Bun": [99]
}
for names, numbers in people.items():
    print(f"\n{names}'s favorite number:")
    for number in numbers:
        print(f"\t{number}", end="")
    print()