# Write a program that prompts the user to input a number. 
# Program should display the corresponding days to the number. 
# For example if user type 1 the output should be sunday. If user type 7 the output should be saturday

print("This program will let you know what day of week by enter your number from 1 to 7")
while True:
    num = float(input("Enter a number: "))
    try:
        if num in range(1,8):
            break
    except ValueError:
        continue

num = int(num)
if num == 1 :
    print("Sunday")
elif num == 2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wendnesday")
elif num == 5:
    print("Thursday")
elif num == 6:
    print("Friday")
elif num == 7:
    print("Saturday")
