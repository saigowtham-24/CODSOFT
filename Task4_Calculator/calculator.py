def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error: Division by zero"
    return x/y

def get_numbers():
    try:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        return num1,num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None,None

def calculator():
    print("Simple CLI Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    try: 
        choice=int(input("Enter choice (1/2/3/4): "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        return
    
    if choice in [1,2,3,4]:
        num1,num2=get_numbers()
        if num1 is None or num2 is None:
            return

        operations={
            1:("+",add),
            2:("-",subtract),
            3:("*",multiply),
            4:("/",divide)
        }

        symbol,operation=operations[choice]
        result=operation(num1,num2)
        print(f"{num1} {symbol} {num2} = {result}")
    else:
        print("Invalid choice. Please select from 1 to 4.")

if __name__=="__main__":
    calculator()
