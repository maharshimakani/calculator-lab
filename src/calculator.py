from src import utils


def perform_operation(choice, a, b):
    if choice == "1":
        return utils.add(a, b)
    if choice == "2":
        return utils.subtract(a, b)
    if choice == "3":
        return utils.multiply(a, b)   # Partner B implements
    if choice == "4":
        return utils.divide(a, b)     # Partner B implements
    raise ValueError("Invalid operation choice")


def interactive():
    while True:
        print("Choose operation:\n1) Add  2) Subtract  3) Multiply  4) Divide")
        choice = input("Enter choice (1-4): ").strip()
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = perform_operation(choice, a, b)
        except ValueError as e:
            print("Invalid input:", e)
            continue
        except ZeroDivisionError:
            print("Error: division by zero")
            continue

        print("Result:", result)
        again = input("Another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break
