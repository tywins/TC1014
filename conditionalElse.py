# This is an example of a simple if-else statement in which the program
# checks that the password is "1234"
un = str(input("Enter username: "))
pw = int (input("Enter password: "))

if (pw == 1234):
    print ("Welcome back,", un, "!")
else:
    print ("Something went wrong, check that your username and password are correct.")
