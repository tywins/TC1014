x=int(input("Enter lower bound: "))
y=int(input("Enter upper bound: "))
summ = 0
ct = x
while (ct <= y):
#    print("summ is ", summ)
#    print("ct is ",ct)
#    print()
    summ = summ + ct
    ct = ct + 1
print ("The sum from ", x, " to ", y, " (inclusive) is ", summ)
