user_choice = True
while user_choice:
    print("Choose any of the following options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide\n")

    try:
        func = int(input("Enter your choice (1,2,3 or 4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


    def add(num1,num2):
        return num1 + num2

    def subtract(num1,num2):
        return num1 - num2

    def multiply(num1,num2):
        return num1 * num2

    def divide(num1,num2):
        return num1 / num2


    if func == 1:
        print(add(num1, num2))
    elif func == 2:
        print(subtract(num1, num2))
    elif func == 3:
        print(multiply(num1, num2))
    elif func == 4:
        print(divide(num1, num2))

    user_choice = input("Do you want to continue? (yes/no): ").lower() == 'yes'
    if user_choice == False:
        print("Thank you for using the calculator. Goodbye!")
