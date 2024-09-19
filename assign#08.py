def add(a, b):
    """Adding two numbers"""
    return a + b
def subtract(a, b):
    """Subtracting two numbers"""
    return a - b
def multiply(a, b):
    """Multiplying two numbers"""
    return a * b
def divide (a, b):
    """Dividing two numbers handling division by zero"""
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a / b
def calculate():
    """Main calculator functions"""
    print("Welcome to the calculator!")
    print("Choose any operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter your choice from the above (1/2/3/4):")

    if choice not in ['1','2','3','4']:
        print("Invalid choice, Please enter a number from 1 to 4")
        return
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
    print("Result:", result)

# Main program loop
while True:
    calculate()
    print("Do you want to perform another calculation? (yes/no)")
    if input().lower() != "yes":
        break