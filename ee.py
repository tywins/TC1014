def estimatinge(x):
    a = x
    b = (1+1/a)**a
    return float(b)

c = int(input("Number of decimal points of accuracy: "))

ans = estimatinge(x)

print("The estimate of the constant e is:",ans)
