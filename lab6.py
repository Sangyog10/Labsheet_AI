#calculate factorial
def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)


val = int(input("Enter a number\n"))
print(fact(val))