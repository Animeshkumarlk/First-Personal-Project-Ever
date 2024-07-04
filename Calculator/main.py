
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else None

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# Take user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform selected operation and display result
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    if result is not None:
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid Input")
