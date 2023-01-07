# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. 
#   Add a print() call to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person
guests = ["Vi", "Nhat", "Hoa"]

takeout_person = guests.pop(2)
print(f"{takeout_person} said she cannot come.")

guests.append("Mo")
for i in range(len(guests)):
    print(f"Hi {guests[i]}, I would like to invite you for a Thansgiving dinner on next week.")

print("I found the bigger didnner table, so more space is available")

guests.insert(0,"Kim")
guests.insert(2,"My")
guests.append("An")
for i in range(len(guests)):
    print(f"Hi {guests[i]}, I would like to invite you for a Thansgiving dinner on next week.")

