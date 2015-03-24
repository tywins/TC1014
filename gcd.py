#Paulina Romo Villalobos
def gcd(n,m):
    if(n == m):
        answer = n
    elif(n > m):
        answer = gcd((n-m), m)
    else:
        answer = gcd(n, (m-n))
    return answer

x = int(input("First number: "))
y = int(input("Second number "))
gcdiv = gcd(n, m)
print("GCD of", x , "and", y, ": ", gcdiv)
