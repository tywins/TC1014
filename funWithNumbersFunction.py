#Paulina Romo Villalobos
#This program sums two integers given by the user

def integersum (a,b):
    ans = a + b
    return ans;

def integerdiff (a,b):
    ans = a - b
    return ans;

def integerprod (a,b):
    ans = a * b
    return ans;

def integerdiv (a,b):
    ans = a / b
    return ans;

def integerrem (a,b):
    ans = a % b
    return ans;

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))

summ = integersum(x,y)
diff = integerdiff(x,y)
prod = integerprod(x,y)
division = integerdiv(x,y)
remainder = integerrem(x,y)

print ("The sum of those numbers is ", summ)
print ("The difference of those numbers is ", diff)
print ("The product of those numbers is ", prod)
print ("The division of those numbers is ", division)
print ("The remainder of those numbers is ", remainder)
