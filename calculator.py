def calculate(num1,num2,operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2==0:
            return "Cannot be divided by ZERO"    
        return num1/num2

while True:
    print("1. Calculator")
    print("2. Clear")
    print("3. Exit")

    choice=input("Enter the choice: ")
    if choice=="1":
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        operator=input("Enter the operator (+ - * /): ")

        result=calculate(num1,num2,operator)
        print("Result: ",result)
    elif choice=="2":
        print("Calculator Cleared")
    elif choice=="3":
        print("GOOD BYE")
        break
    else:
        print("Invalid Choice")
        