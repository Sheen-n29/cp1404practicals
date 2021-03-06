"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_of_months = int(input("How many months? "))

    for num_of_months in range(1, num_of_months + 1):
        income = float(input("Enter income for month {}: ".format(str(num_of_months))))
        incomes.append(income)

    display_report(incomes, num_of_months)


def display_report(incomes, num_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for num_of_months in range(1, num_of_months + 1):
        income = incomes[num_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(num_of_months, income, total))


main()
