#This program sums a range of numbers *not inclusive
n = int(input("Start range from: "))
e = int(input("End range at (exclusive): "))
s = 0
for i in range (n,e):
    s += i
    print("Result: ",s)
