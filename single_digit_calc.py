a=input("SINGLE DIGIT CALCULATOR - Write down what you  want to calculate: ")

if a[1] == "+":
    print(int(a[0])+int(a[2]))
elif a[1] == "-":
    print(int(a[0])-int(a[2]))
elif a[1] == "*":
    print(int(a[0])*int(a[2]))
elif a[1] == "/":
    print(int(a[0])/int(a[2]))
else:
    print("Sorry, ", a, " contains an unknown operation for me.")