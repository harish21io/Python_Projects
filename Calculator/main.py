import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError ("Cannot Divide by 0")
    else:
        return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    print(art.logo)
    while True:
        try:
            num1 = float(input("Enter your first number: "))
            break
        except ValueError:
            print("Enter only Integer or Float")

    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operators = input("Pick an operation:\n")
        if operators not in operations:
            print(f"Error: {operators} is undefined")
            continue
        while True:
            try:
                num2 = float(input("Enter your second number: "))
                break
            except ValueError:
                print("Enter only Integer or Float")
        try:
            result = operations[operators](num1,num2)
        except KeyError:
            print(f"{operators} not in defined list")
            return
        except ZeroDivisionError:
            print("Cannot Divide by 0")
            return
        print(f"{num1} {operators} {num2} = {result}")
        continue_calc = input(f"Type 'y' to continue calculating with {result} "
                              f"or type 'n' to start a new calculation: ").lower()
        if continue_calc == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()
