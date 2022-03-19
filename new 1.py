num1=int(input("enter the first number"))
op=input("operator")
num2=int(input("enter the second number"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else :
    print("invalid operation")