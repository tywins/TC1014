x=float(input("Enter a temperature in Fahrenheit: "))
celsius=5.0 * (x - 32.0)/9.0
print ("A temperature of ", x, " degrees Fahrenheit is ", celsius, " in Celsius")
if (celsius>=100):
    print ("Water boils at this temperature.")
else:
    print ("Water does not boil at this temperature.")
