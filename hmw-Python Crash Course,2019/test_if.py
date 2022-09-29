age = int(input("Age: "))
if age < 2:
    print("You are a baby.")
elif age in range(2,4):
    print("You are a toddler.")
elif age in range(4,13):
    print("You are a kid.")
