"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_month = int(input("How many months? "))

    for month in range(1, num_month + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)
    # display_report(incomes, num_month)
    display_report_with_enumerate(incomes)

def display_report(incomes, num_month):
    """Display report in a formatted way."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f}\t\tTotal: ${:10.2f}".format(month, income, total))


def display_report_with_enumerate(incomes):
    """Display report in a formatted way."""
    print("\nIncome Report\n-------------")
    total = 0
    for index, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f}\t\tTotal: ${:10.2f}".format(index + 1, income, total))


main()
