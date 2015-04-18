def fib(x):
    n = x
    m = y
    if (n == 0 or n == 1):
        return n
    if (n > 1):
        f = fib(m - 2) + fib(n - 1)
        return f
        
x = int(input("Insert lower bound: "))
y = int(input("Insert upper bound: "))

fc = fib(x)

print ("The fibonacci sequence of ", x, " to ", y, " is: ", fc)
