# Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
#• Use a conditional test in the while statement to stop the loop.
#• Use an active variable to control how long the loop runs.
#• Use a break statement to exit the loop when the user enters a 'quit' value

message = ""
while message != "quit":
    message = input("Enter your age: ")
    if message != "quit":
        age = int(message)
        if age < 3:
            print("Your ticket is free")
        elif age <= 12:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15")
    else:
        break
