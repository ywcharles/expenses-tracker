'''
 file: main.py
 purpose: check expenses from a certain time period or a certain category
 author: Charles Wu
'''

# imports
from tools import displayOptions, getValidInt
from sqltools import insertExpense, displayAllExpenses, displayAllCategories, deleteExpense
from sqltools import displayLastWeekExpenses, displayMonthlyExpenses, displayMonthlyCategoryExpenses

if __name__ == "__main__":
    while True:
        displayOptions()
        print("Choose an option from above: ")
        user_choice = getValidInt()
        if user_choice == 1:
            insertExpense()

        elif user_choice == 2:
            displayLastWeekExpenses()

        elif user_choice == 3:
            displayMonthlyExpenses()

        elif user_choice == 4:
            displayAllCategories()

        elif user_choice == 5:
            displayMonthlyCategoryExpenses()

        elif user_choice == 6:
            displayAllExpenses()

        elif user_choice == 7:
            deleteExpense()

        elif user_choice == 8:
            print("You exited the program.")
            break

        else:
            print("Invalid option! Please try again.")
