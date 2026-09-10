print("======SIMPLE CALCULATOR=====")
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
choice = int(input("Enter your choice: "))

def Add():
    sum= num1 + num2
    print("Addition:" ,sum)

def Sub():
    diff = num1- num2
    print("Subtraction: ", diff)

def Multiply():
    mult=num1*num2
    print("Multiplication:", mult)


def Division():
    if num1 == 0 or num2 == 0:
        print("Error: Division by zero is not allowed.")
    elif num2 > num1:
        div = num2 / num1
        print("Division:", div)
    else:
        div = num1 / num2
        print("Division:", div)
    
match choice:
    case 1:
        Add()

    case 2:
        Sub()

    case 3:
        Multiply()

    case 4:
        Division()

    case _:
        print("Invalid Choice")
