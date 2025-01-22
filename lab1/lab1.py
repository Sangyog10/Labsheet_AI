
def checkNum( val):
    if(val % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")

val = input("Enter a number\n")
checkNum(int(val))