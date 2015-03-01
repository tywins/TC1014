import random
value=random.randint(1, 100)

text=input("Insert any number: ")
number=int(text)

while(number !=value):
    if number>value:
        print("Too high")
    else:
        print("Too low")
    text=input("Give me another number.")
    number=int(text)

print ("Your guessed the number!")
