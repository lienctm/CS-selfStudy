# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
#  • Start with your program from Exercise 3-4. 
guests = ["Vi", "Nhat", "Hoa"]
for i in range(len(guests)):
    print(f"Hi {guests[i]}, I would like to invite you for a Thansgiving dinner on next week.")

#   Add a print() call at the end of your program stating the name of the guest who can’t make it.
takeout_person = guests.pop(2)
print(f"{takeout_person} said she cannot come.")

#  • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
guests.append("Mo")

#  • Print a second set of invitation messages, one for each person who is still in your list.
for i in range(len(guests)):
    print(f"Hi {guests[i]}, I would like to invite you for a Thansgiving dinner on next week.")
