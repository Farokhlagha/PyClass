import math

print("welcome to Far calculator.")

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("log")
print("sin")
print("tan")
print("exit")
print("Enter your operation: ")
op = input()

if op =="+" or op == "-" or op == "*" or op == "/":
    a = float(input("enter first num: "))
    b = float(input("enter second num: "))
else:
    a = float(input("enter first num: "))

if op == "=":
    result = a + b

elif op == "-":
    result = a - b

elif op =="*":
    result = a * b

elif op == "/":
    if b == 0:
        result = "can not divided by zero!"
    else:
        result = a / b

elif op == "sin":
    result = math.sin(a)

elif op == "log":
    result = math.log(a)


print(result)