x = float(input("Enter your first number:"))

y = input("Enter your operator {+,-,*,/,%}:")

z = float(input("Enter your second number:"))

if y=="+":
    print("Your answer is :",x+z)

elif y=="-":
    print("Your answer is :",x-z)

elif y=="*":
    print("Your answer is :",x*z)

elif y=="/":
    print("Your answer is :",x/z)

elif y=="%":
    print("Your answer is :",x%z)

else:
    print(" Sorry!! Invalid operator")