#This program lists a range of numbers, then allows you to
# see the series of said range that goes up by an integer introduced
# by the user *not inclusive
n = int(input("Start range from: "))
e = int(input("End range at (exclusive): "))
b = int(input("Go up by: "))

for i in range (n,e):
    print (i)

for i in range (n,e, b):
    print (i)
