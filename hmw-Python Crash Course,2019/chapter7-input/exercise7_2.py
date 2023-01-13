# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message say- ing they’ll have to wait for a table. 
# Otherwise, report that their table is ready.

prompt = int(input("How many people are in your dinner group? "))
if prompt >= 8 :
    print("Please wait for a bigger table")
else:
    print("Your table is ready")