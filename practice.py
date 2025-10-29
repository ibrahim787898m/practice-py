op = input("operator: ")
x = int(input("x: "))
y = int(input("y: "))

if op == '+':
    print("answer: ", x + y)
elif op == '-':
    print("answer: ", x - y)
elif op == '*':
    print("answer: ", x * y)
elif op == '/':
    print("answer: ", x / y)
else:
    print("invalid operator")