# you are required to create a simple calculator program that can add,
# subtract, multiply or divide input from the user
# Extend your program by displaying an error message when the user enters an invalid input
# Extend your program by making it run continuously until the user wants to stop:
# you should print out a message that asks if the user wants to do another operation:
# If the answer is "yes" then the previous menu should be displayed again.
# If the answer is "no" then the program stops.

def add(n,m):
    print(n+m)
def subtract(n,m):
    print(n-m)
def multiply(n,m):
    print(n*m)
def divide(n,m):
    print(n/m)
def exponent(n,m):
    print(n**m)
def modulus(n,m):
    print(n%m)

operand = 1
operation = int(input("Select an operation:\n(1) Add\n(2) Subtract\n(3) Multiply\n(4) Divide\n(5) Exponentiation\n(6) Modulus\n"))
while operand == 1:
    if operation == 1:
        n = int(input("First number"))
        m = int(input("Second number"))
        add(n,m)
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
    elif operation == 2:
        n = int(input("First number"))
        m = int(input("Second number"))
        subtract(n,m)
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
    elif operation == 3:
        n = int(input("First number"))
        m = int(input("Second number"))
        multiply(n,m)
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
    elif operation == 4:
        n = int(input("First number"))
        m = int(input("Second number"))
        divide(n,m)
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
    elif operation == 5:
        n = int(input("First number"))
        m = int(input("Second number"))
        exponent(n,m)
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
    elif operation == 6:
        n = int(input("First number"))
        m = int(input("Second number"))
        modulus(n,m)
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
    else:
        print("Invalid option")
        operand = int(input("Would you like to continue?\n(1) Yes\n(2) No\n"))
print("Goodbye!")