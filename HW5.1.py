while True:
    print("Hello, I am a simple calculator")
    num1 = int(input("Enter number 1: "))
    operator = input("Enter operator (1 +, 2 -, 3 *, 4 /): ")
    num2 = int(input("Enter number 2: "))

    if operator == '1':
        print(num1 + num2)
    elif operator == '2':
        print(num1 - num2)
    elif operator == '3':
        print(num1 * num2)
    elif operator == '4':
        print(num1 / num2)
    else:
        print("Invalid operator")

    The_end = input("Do you want to continue? (Yes or Y to continue): ").lower()
    if The_end != 'yes' and The_end != 'y':
        print("Exiting the calculator. Goodbye!")
        break

