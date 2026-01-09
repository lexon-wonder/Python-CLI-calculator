while True:
    first_number = float(input("input your first number:"))
    operator = input ("please input the operator(+,-, /,*,):")
    second_number = float(input("input your second number:"))
    message = "Invalid operator! Please try a valid operator"
    if operator =="+":
        print(f"your answer is {first_number + second_number}")
    elif operator == "-":
        print(f"your answer is {first_number - second_number}")
    elif operator == "*":
            print(f"your answer is {first_number * second_number}")
    elif operator == "/":
        if second_number != 0:
            print(f"your answer is {first_number / second_number}")
        else:
            print("Math Error: you cannot divide a number by zero.")
    else:
        print(message)
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        print("Goodbye calc buddy!")
        break





