def main():
    dash()
    print("Welcome to simple calculator app!")
    dash()
    print("You can do 4 type of operation here: ")
    print("1. Type + for addition")
    print("2. Type - for substraction")
    print("3. Type * for multiplication")
    print("4. Type / for division")
    dash()

    while True:
        op = input("Operation: ")
        x = float(input("X: "))
        y = float(input("Y: "))

        if op == "+":
            print("Answer:", addition(x, y))
        elif op == "-":
            print("Answer:", subtraction(x, y))
        elif op == "*":
            print("Answer:", multiplication(x, y))
        elif op == "/":
            print("Answer:", division(x, y))

        dash()

        res = input("Do you wanna continue(y/n): ")

        dash()

        if res.lower() == "n":
            print("Thank you for using simple calculator!")
            dash()
            break

        elif res.lower() == "y":
            continue

def dash():
    print("-" * 40)

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    main()