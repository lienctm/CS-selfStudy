# Ask the user for a number, and then report whether the number is a multiple of 10 or not.
prompt = int(input("Enter a number: "))
if prompt % 10 == 0 :
    print(f"{prompt} is a multiple of 10")
else:
   print(f"{prompt} is not a multiple of 10") 