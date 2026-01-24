choice=0
while choice!=3:
    print("1-add two numbers")
    print("2-subtract two numbers")
    print("3-exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        num1=int(input("Enter your first number : "))
        num2=int(input("Enter your second number : "))
        print("Result : ", num1+num2)
    elif choice==2:
        num1=int(input("Enter your first number : "))
        num2=int(input("Enter your second number : "))
        print("Result : ", num1-num2)
    elif choice==3:
        print("Exiting")
