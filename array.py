from array import *

number = array("f", [20.5, 40, 50, 10, 90,10])

c = number.append(3000)  # append a number in the last of the array
print(number)

d = number.remove(3000)  # remove a number in the last of the array
print(number)

e = number.reverse()     # reverse the full array
print(number)

f = number.pop(2)        # delete or pop a number from the defined position
print(number)

g = number.index(50)     # get the index number of the defined element
print(g)

h = number.count(10)     # the defined element total  number
print(h)
