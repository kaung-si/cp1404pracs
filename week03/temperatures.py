"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    """Temperature Conversion Program"""
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_valid_input("Celsius")
            print("Result: {:.2f} F".format(convert_to_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = get_valid_input("Fahrenheit")
            print("Result: {:.2f} F".format(convert_to_celsius(fahrenheit)))
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_input(prompt):
    value_input = False
    while not value_input:
        try:
            num = float(input("Enter {}: ".format(prompt)))
            value_input = True
            return num
        except ValueError:
            print("Enter a valid input.")


def display_menu():
    """Display instruction menu"""
    print("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit""")


def convert_to_fahrenheit(c):
    """Calculate Fahrenheit to Celsius."""
    return c * 9.0 / 5 + 32


def convert_to_celsius(f):
    """Calculate Celsius to Fahrenheit"""
    return 5 / 9 * (f - 32)


main()
