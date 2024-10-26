def calculator():
    print("select operation:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")

    OneToFour = ['1', '2', '3', '4']

    choice = (input("Enter choice (1/2/3/4): "))


    if choice in OneToFour:
        N1 = float(input("please enter first number: "))
        N2 = float(input("please enter second number: "))
       
        if choice == '1':
            print(f"result: {N1} + {N2} = {(N1 + N2)}")
        
        elif choice == '2':
            print(f"result: {N1} - {N2} = {(N1 - N2)}")

        elif choice == '3':
            print(f"result: {N1} * {N2} = {(N1 * N2)}")

        elif choice == '4':
            try:
                print(f"result: {N1} / {N2} = {(N1 / N2)}")
            except ZeroDivisionError:
                print("Error! Division by zero.")
    else:
        print("please enter a valid option!! ")

            
calculator()

