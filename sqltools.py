'''
    file: sqltools.py
    purpose: create tools that would assist in searching/adding in a SQL database
    author: Charles Wu
'''

# imports
from expense import Expense
import mysql.connector
from tools import getExpenseInput, getValidInt, exportExpensesToCSV, exportCategoriesToCSV
from datetime import date

# open database
# PLEASE ENTER HOST, USER, PASSWORD AND DATABASE
expenses_db = mysql.connector.connect(
  host="***INSERT HOST HERE***",
  user="***INSERT USER HERE***",
  password="***INSERT PASSWORD HERE***",
  database="***INSERT DATABASE HERE***"
)

# create cursor
my_cursor = expenses_db.cursor(buffered=True)

# functions
def printExpensesTable(expenses):
    '''
    Print a formatted expenses table
    :param expenses: expenses list
    '''
    print(f'ID    | AMOUNT   | REASON                   | DATE(YYYY-MM-DD) | CATEGORY       ')
    print(f'--------------------------------------------------------------------------------')
    for expense in expenses:
        # get category name
        my_cursor.execute(f"SELECT category_name FROM categories WHERE category_id = {expense[4]};")

        ID = expense[0]
        amount = expense[1]
        reason = expense[2]
        date = expense[3]
        category = my_cursor.fetchall()[0][0]

        # display formatted data
        print(f"{ID:<6}| {amount:<9}| {reason:<25}| {date}       | {category}")
    print(f'-------------------------------------------------------------------------------')

def printCategoriesTable(categories):
    '''
    Print a formatted table for the categories
    :param categories: categories list
    '''
    # print table header
    print(f"ID    | CATEGORY NAME          | TOTAL EXPENSES")
    print(f"-----------------------------------------------")

    for category in categories:
        category_id = category[0]
        category_name = category[1]
        total_expense = category[2]
        print(f"{category_id:<6}| {category_name:<23}| {total_expense}")
    print(f"-----------------------------------------------")

def checkCategory(expense):
    '''
    Check if categories exits or not
    :param expense: expense object inputted by user
    '''
    category = expense.getCategory()

    # search for category in the database
    my_cursor.execute(f"SELECT category_name FROM categories "
                      f"WHERE category_name = '{category}';")
    my_result = my_cursor.fetchall()

    # if any result is found
    if my_result:
      category_exists = True

    # if no result is found
    else:
      category_exists = False
    return category_exists

def getCategoryID(expense):
    '''
    Get the id from the category that the expense belongs
    :param expense: expense object
    :return: category's ID
    '''
    category = expense.getCategory()
    if not checkCategory(expense):
      # insert new category if category is not found
      my_cursor.execute(f"INSERT INTO categories (category_name, total_expenses)"
                        f"VALUES ('{category}',0);")
      expenses_db.commit()

    # search for the category id in the database
    my_cursor.execute(f"SELECT category_id "
                      f"FROM categories "
                      f"WHERE category_name = '{category}';")
    category_id = my_cursor.fetchall()
    return category_id[0][0]

def incrementCategoryTotal(expense):
    '''
    Increment the total expenses from a category
    :param expense: expense object
    '''
    category_id = getCategoryID(expense)
    expense_amount = expense.getAmount()

    # get total expenses
    my_cursor.execute(f"SELECT total_expenses FROM categories "
                      f"WHERE category_id = {category_id}")
    total_expenses = float(my_cursor.fetchall()[0][0])
    total_expenses += expense_amount

    # increment total expenses
    my_cursor.execute(f"UPDATE categories SET total_expenses = {total_expenses} "
                      f"WHERE category_id = {category_id}")
    expenses_db.commit()

def insertExpense():
    user_input = getExpenseInput()

    # increment category's total value
    incrementCategoryTotal(user_input)

    # data
    amount = user_input.getAmount()
    reason = user_input.getReason()
    date = user_input.getDate()
    category_id = getCategoryID(user_input)
    my_cursor.execute(f"INSERT INTO expenses (amount, reason, expense_date, category_id)"
                      f"VALUES ({amount}, '{reason}', '{date}', {category_id});")
    expenses_db.commit()

def displayAllExpenses():
    '''
    Display all the expenses as a formatted table
    '''
    # select all the expenses data
    my_cursor.execute(f'SELECT * FROM expenses;')
    all_expenses = my_cursor.fetchall()
    printExpensesTable(all_expenses)
    print('\n')

    # format filename
    weeks_date = str((date.today()))
    weeks_date.replace('-','_')
    exportExpensesToCSV(all_expenses, f'all_expenses_{weeks_date}')

def displayAllCategories():
    my_cursor.execute(f"SELECT * FROM categories;")
    all_categories = my_cursor.fetchall()
    printCategoriesTable(all_categories)


    # format filename
    weeks_date = str((date.today()))
    weeks_date.replace('-','_')
    exportCategoriesToCSV(all_categories, f'all_categories_{weeks_date}')
    print('\n')

def displayLastWeekExpenses():
    '''
    Display last weeks expense's table
    '''
    # select last weeks data from table
    my_cursor.execute(f"SELECT * FROM expenses WHERE expense_date BETWEEN date_sub(now(),INTERVAL 1 WEEK) AND now();")
    last_week_expenses = my_cursor.fetchall()
    printExpensesTable(last_week_expenses)

    # format filename
    weeks_date = str((date.today()))
    weeks_date.replace('-','_')
    filename = f"weekly_expenses_{weeks_date}"
    exportExpensesToCSV(last_week_expenses, filename)
    print('\n')

def displayMonthlyExpenses():
    '''
    Display monthly expenses table
    '''
    # get month and year
    print("Please insert the month(MM) from the expenses: ")
    month = getValidInt()
    print("Please insert the year(YYYY) from the expenses: ")
    year = getValidInt()
    month_date = f"{year}-{month:02d}"

    # get expenses on that month
    my_cursor.execute(f"SELECT * FROM expenses WHERE expense_date LIKE '{month_date}%';")
    month_expenses = my_cursor.fetchall()

    printExpensesTable(month_expenses)

    # format filename
    months_date = str((date.today()))
    months_date.replace('-','_')
    filename = f"monthly_expenses_{months_date}"
    exportExpensesToCSV(month_expenses, filename)
    print('\n')

def displayMonthlyCategoryExpenses():
    '''
    Display a category's expenses in a month
    '''
    # get date
    print("Please insert the month(MM) from the expenses: ")
    month = getValidInt()
    print("Please insert the year(YYYY) from the expenses: ")
    year = getValidInt()
    month_date = f"{year}-{month:02d}"

    # display categories and get ID
    my_cursor.execute(f"SELECT * FROM categories;")
    all_categories = my_cursor.fetchall()
    printCategoriesTable(all_categories)
    print("Please insert the category's ID: ")
    category_id = getValidInt()

    # display data
    my_cursor.execute(f"SELECT * FROM expenses WHERE (expense_date LIKE '{month_date}%' AND category_id = {category_id});")
    categories_monthly_expenses = my_cursor.fetchall()
    if categories_monthly_expenses:
        printExpensesTable(categories_monthly_expenses)

        # format filename
        weeks_date = str((date.today()))
        weeks_date.replace('-', '_')
        filename = f"category_{category_id}_monthly_expenses_{weeks_date}"

        exportExpensesToCSV(categories_monthly_expenses, filename)
        print("\n")
    else:
        print(f"The category with the inputted ID was not found. \n")

def deleteExpense():
    '''
    Delete an expense inputted
    '''
    # get expense ID
    print("Please insert the ID from the expense you want to be deleted: ")
    expense_id = getValidInt()

    # get amount and category ID
    my_cursor.execute(f"SELECT amount, category_id FROM expenses WHERE expense_id = {expense_id};")
    expense_data = my_cursor.fetchall()
    if expense_data:
        expense_amount, category_id = expense_data[0]

        # get total expenses
        my_cursor.execute(f"SELECT total_expenses FROM categories "
                          f"WHERE category_id = {category_id}")
        total_expenses = my_cursor.fetchall()[0][0]

        # decrement total expenses
        total_expenses -= expense_amount
        my_cursor.execute(f"UPDATE categories SET total_expenses = {total_expenses} "
                          f"WHERE category_id = {category_id}")
        expenses_db.commit()

        # delete expense
        my_cursor.execute(f"DELETE FROM expenses WHERE expense_id = {expense_id};")
        expenses_db.commit()
        print(f"The expense with ID {expense_id} was deleted")

    else:
        print(f"The expense with the inputted ID was not found. \n")



if __name__ == "__main__":
    displayAllExpenses()

