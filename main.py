# Program Comments
# Written by: Jennifer Oliver
# Date Written: July 17, 2023 - July 25, 2023
# Description: Total Monthly Sales Line Graph

# Program imports.
import matplotlib.pyplot as plt
import FormatValues as FV

# Main Program.
# Graph a table showing total sales per month
Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

while True:
    # creates a loop so the user can input multiple graphs in a row.
    Sales = []

    for Month in Months:
        MonthSales = input(f"Enter total sales for the month of {Month}, 2023: ")

        Sales.append(FV.FDollar2(float(MonthSales)))

    plt.plot(Months[:len(Sales)], Sales)
    plt.title("TOTAL SALES PER MONTH", color="purple")
    plt.xlabel("MONTH", color="purple")
    plt.gca().tick_params(axis='x', colors='blue')
    plt.ylabel("TOTAL SALES ($)", color="purple")
    plt.gca().tick_params(axis='y', colors='green')
    plt.show()

    # Allows the user to end the program.
    Restart = input("Do you want to continue? (Y/N): ")
    if Restart.upper() != "Y":
        break
