
#operation functions
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def power(a,b):
    return a ** b

def divide(a,b):
    if b == 0:
        return("Math Error! You cannot divide a number by zero.")
    else:
        return a / b
    
def modulo(a,b):
    if b == 0:
        return("Math Error! You cannot modulo a number by zero.")
    else:
        return a % b

#input functions
def get_numbers():
    try:
        a = float(input("input your first number:"))
        b = float(input("input your second number:"))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None
    

    
#Menu function
def show_menu():
    print("\n === SIMPLE CALCULATOR===")
    print("+ or add ➡ addition ")
    print("- or sub ➡ subtraction ")
    print("* or mul ➡ multiplication ")
    print("/ or div ➡ division ")
    print("% or sub ➡ modulo/reminder ")
    print("** or pow ➡ power ")
    print("To close the calculator program, type \"stop\" in the operator entry.")

#operator function
def operator():
    sign = input("Please input the operator")
    return sign


#Calculator logic
def calculator(a,b,op):
    if op == ("+") or op.lower() ==("add"):
        print(f"answer: {add(a,b)}")
    elif op == ("-") or op.lower() ==("sub"):
        print(f"answer: {subtract(a,b)}")
    elif op == ("*") or op.lower() ==("mul"):
        print(f"answer: {multiply(a,b)}")
    elif op == ("/") or op.lower() ==("div"):
        print(f"answer: {divide(a,b)}")
    elif op == ("%") or op.lower() ==("mod"):
        print(f"answer: {modulo(a,b)}")
    elif op == ("**") or op.lower() ==("pow"):
        print(f"answer: {power(a,b)}")
    elif op.lower() == ("stop"):
        print("")
    else:
        print("Invalid Operator! Please input a valid operator.")

#final execution of the calculator
while True:
    show_menu()
    a, b = get_numbers()
    if a == None or b == None:
        continue
    else:
      op = operator()
      calculator(a,b,op)
    if op.lower() == "stop":
        print("CALCULATOR 1.2 CLOSING ...")
        break
    
