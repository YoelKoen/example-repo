"""
This module implements a simple calculator application that allows users to
perform basic arithmetic operations and record/view a history of calculations.
"""
def perform_calculation():
    """
    Performs a calculation based on user input and records it to equations.txt.
    Includes defensive programming for robust input handling.
    """
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    result = None
    equation = ""

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please use +, -, *, or /.")
        return

    equation = f"{num1} {operation} {num2} = {result}"
    print(f"Result: {result}")

    try:
        with open("equations.txt", "a", encoding='utf-8') as file:
            file.write(equation + "\n")
        print("Calculation recorded successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

def print_previous_calculations():
    """
    Reads and prints previous calculations from equations.txt.
    Includes defensive coding to handle the case where the file does not exist.
    """
    try:
        with open("equations.txt", "r", encoding='utf-8') as file:
            print("\n--- Previous Calculations ---")
            content = file.read()
            if content:
                print(content.strip())
            else:
                print("No previous calculations found.")
            print("---------------------------")
    except FileNotFoundError:
        print("\nNo previous calculations found (equations.txt does not exist).")
    except IOError as e:
        print(f"Error reading file: {e}")

def main():
    """
    Main function to run the calculator application.
    Allows users to choose between performing a calculation or viewing history.
    """
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Perform a calculation")
        print("2. Print previous calculations")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_calculations()
        elif choice == '3':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
