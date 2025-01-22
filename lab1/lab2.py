def calc(percentage):
    if(percentage>=80):
        print("Distinction")
    elif(percentage>=65):
        print("First division")
    elif(percentage>=55):
        print("Second divison")
    elif(percentage>=40):
        print("Third division")
    else:
        print("Fail")



percentage = input("Enter the percentage\n")
calc(int(percentage))
