# Write a program that polls users about their dream vaca- tion.
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll
vacations = []
active = True
while active:
    prompt = input("If you could visit one place in the world, where would you go? ")
    vacations.append(prompt)
    response = input("Do you want to continue? ") 
    if response.lower() in 'no':
        active = False
print("\n----Poll results----")
for vacation in vacations:
    print(vacation)