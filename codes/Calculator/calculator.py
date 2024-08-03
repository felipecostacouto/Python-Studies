def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_operator():

    operators = ("+", "-" , "*", "/")
    while True:
        operator = input("Pick an operation (+, -, *, /):\n")
        if operator in operators:
            return operator
        else:
            print("Invalid operator. Please choose from +, -, *, /")
        
def calculate(first, second, operator):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "/":
        return first / second


def main():
    first = get_number("What`s the firt number? \n")
    should_continue = True
    while should_continue:
        operator = get_operator()
        second = get_number("What`s the second number? \n")
        result = calculate(first,second,operator)
        print(f"\nThe result of {first} {operator} {second} is: {result}")
        if input(f"Type 'y' to continue calculationg with {result}, or type 'n' to start a new calculation: ") == "y":
            first = result
        else:
            should_continue = False
            main()

if __name__ == "__main__":
    main()