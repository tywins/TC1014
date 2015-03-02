#Paulina Romo Villalobos

import statistics

def totalsum (m):
    tot = 0
    # add to total each value in m
    for indice in range(len(m)):
        tot = tot + m[indice]
    return tot

def average (m):
    av = mitotal / 10.0
    return av

def standevi (m):
    sd = statistics.stdev(l)
    return sd

l=[]
x = 0

while (x < 10):
    x = x + 1
    n = float(input("Give me a number: "))
    l.append(n)
    mitotal = totalsum(l)
    promedio = average(l)
devi = standevi(l)

print ("No more values.")
print ("Total sum: ", mitotal)
print ("Average: ", promedio)
print ("Stardard deviation: ", devi)
