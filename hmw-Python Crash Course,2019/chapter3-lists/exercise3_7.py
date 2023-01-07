# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can
#   invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list.
#   Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. 
#   Print your list to make sure you actually have an empty list at the end of your program.

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

print("I have just received a message that the dinner table won't arrive in time, so I have space for only two")
print("My current list is : ")
print(guests)

remove_guest_list = []
person_1 = guests.pop(0)
remove_guest_list.append(person_1)
person_2 = guests.pop(1)
remove_guest_list.append(person_2)
person_3 = guests.pop(2)
remove_guest_list.append(person_3)
person_4 = guests.pop(2)
remove_guest_list.append(person_4)

for i in range(len(remove_guest_list)):
    print(f"Sorry {remove_guest_list[i]}, I cannot invite you to the dinner")

print("My list after remove some guests is : ")
print(guests)

del guests[1]
del guests[0]

print("My list after remove all guests is : ")
print(guests)

