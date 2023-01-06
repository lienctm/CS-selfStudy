# Write a while loop that asks people why they like programming. Each time someone enters a reason,
# add their reason to a file that stores all the responses.

while True:
    reason = input("Why do you like programming? ")
    if reason != "":
        file_name = 'reason_file.txt'
        with open(file_name, 'a') as file:
            file.write(f'{reason}\n')
    else:
        break
