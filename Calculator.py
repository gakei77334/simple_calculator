# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():    
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    
    for key in operations:
        print(key)
    
    symbol = input("Pick an operation from the line above: ")
    
    answer = operations[symbol](num1, num2)
    
    print(f"{num1} {symbol} {num2} = {answer}")
    
    restart = True
    
    while restart:
    
        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    
        if keep_going != 'y':
            restart = False
            calculator()
    
        symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        new_answer = operations[symbol](answer, next_number)
        print(f"{answer} {symbol} {next_number} = {new_answer} ")
        answer = new_answer

calculator()