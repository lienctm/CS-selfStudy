# Make a list or tuple containing a series of 10 numbers and five letters.
# Randomly select four numbers or letters from the list and print a message saying that any ticket matching
# these four numbers or letters wins a prize.
from random import choice

my_ticket = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
lotery = [0, 2, 'c', 'd']
randomChoice = choice(my_ticket)
if randomChoice in lotery:
    print("You win a prize")
else:
    print("You loose")
