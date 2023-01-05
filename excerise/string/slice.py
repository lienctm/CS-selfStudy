# manipulating python string
# slice string : list[start: end: step]
# start: where you want the slicing to begin
# stop: until where you want the slicing to go, but the value of stop is not included
# if you want to skip an item, the default being 1
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 |#
# +---+---+---+---+---+---+---+
# | h | o | l | i | d | a | y |
# +---+---+---+---+---+---+---+
# | -7| -6| -5| -4| -3| -2| -1|

word = "holiday"

print(word[1:4]) # print "oli"
print(word[:2]) # print "ho"

print(word[-1]) # print "y"
print(word[-2]) # print "a"

print(word[::2]) # print "hldy"

length = len(word)
x = 0 -length
print(x)