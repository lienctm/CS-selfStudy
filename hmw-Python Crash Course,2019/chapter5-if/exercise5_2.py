# You don’t have to limit the number of tests you create to ten. 
# If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
# Have at least one True and one False result for each of the following:
#• Tests for equality and inequality with strings
text0 = "Happy New Year"
text1 = "Happy Wedding"
if text0 == text1:
    print("True. These texts are matched")
else:
    print("False. These texts are different")

#• Tests using the lower() method
if text0 == "Happy New Year":
    print(text0.upper())
else:
    print(text0.lower())

#• Numerical tests involving equality and inequality, greater than and less than,
#  greater than or equal to, and less than or equal to
num1 = 20
num2 = 32
if num1 < num2:
    print("Num2 is greater than num1")
elif num1 > num2:
    print("Num1 is greater than num2")
else:
    print("Num1 is equal to num2")

#• Tests using the and keyword and the or keyword
if num1 > num2 and num2 < num1:
    print("True")
elif num1 > num2 or num2 > num1:
    print("False")

#• Test whether an item is in a list
#• Test whether an item is not in a list
boxes = ["Maya", "Toyota", "student", 22, 12, "December"]
name = "Maya"
num = 21
if name in boxes:
    print(name)
else:
    print(f"{name} does not in the list")

if num in boxes:
    print(num)
else:
    print(f"{num} not in the list")

