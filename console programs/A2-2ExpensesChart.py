#progam that reads data from the file Expenses.txt, puts it into a list
#and displays the expense distribution using a pie chart

#imports
import matplotlib.pyplot as plt

#constants
FILENAME = "Expenses.txt"

def main():
    #gets the expense values as a list to use in a pie chart
    expenses = getExpenses()

    #list of labels for expenses
    expenseLabels = ["Rent", "Gas", "Food", "Clothing", "Car", "Misc"]

    #build pie chart
    plt.pie(expenses, labels=expenseLabels)

    #chart title
    plt.title("Monthly Expenses")

    plt.show()


def getExpenses():
    try:
        inf = open(FILENAME, "r")

        costs = inf.readlines()

        inf.close()

        for index in range(len(costs)):
            costs[index] = costs[index].rstrip("\n")

    except IOError as err:
        print(err)

    except IndexError as err:
        print(err)


    return costs
                           
        


if __name__ == "__main__":
    main()
