def add(a, b):
    c = a + b
    return c


def subtract(a, b):
    c = a - b
    return c


def multiply(a, b):
    c = a * b
    return c


def divide(a, b):
    c = a / b
    return c

x = int(input("Input first number: "))
y = int(input("Input second number: "))
print("")
print("ADD")
print("SUBTRACT")
print("MULTIPLY")
print("DIVIDE")
mode = input("Choose an option: ")
if mode == "ADD":
    answer = add(x, y)
    print(str(answer))
elif mode == "SUBTRACT":
    answer = subtract(x, y)
    print(str(answer))
elif mode == "MULTIPLY":
    answer = multiply(x, y)
    print(str(answer))
elif mode == "DIVIDE":
    answer = divide(x, y)
    print(str(answer))
else:
    print("Invalid mode. Terminating...")
