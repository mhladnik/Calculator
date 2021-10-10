operation = input("Choose the operation you want (+, -, *, /): ")
a = int(input("First number: "))
b = int(input("Second number: "))

if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)
else:
    print("Sorry, ", operation, " is an unknown operation for me.")