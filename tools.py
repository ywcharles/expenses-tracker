'''
 file: tools.py
 purpose: create tools to assist in the main program
 author: Charles Wu
'''

# imports
from expense import Expense

def displayOptions():
    print("1. Insert expense;")
    print("2. Display last week's expenses;")
    print("3. Display expenses by month;")
    print("4. Display by category;")
    print("5. Display category's monthly expenses;")
    print("6. Display all expenses;")
    print("7. Delete an input;")
    print("8. Exit program.")

def getValidInt():
    '''
    Get a valid interger from the user
    :return: interger from the user
    '''
    while True:
        try:
            user_input = int(input())
            break
        except:
            print("Invalid input! Please insert an integer")
    return user_input

def getExpenseInput():
    '''
    Prompt user for data and store them on a expense function
    :return: expense object
    '''
    while True:
        try:
            amount_expended = float(input("Input amount expended: $"))
            break
        except:
            print("Invalid input! please insert a numeric value")
    expense_reason = input("Input the reason why you spent that amount of money: ").lower()
    expense_category = input("Input the expense category: ").lower()
    if amount_expended and expense_reason and expense_category:
        expense_input = Expense(amount_expended, expense_reason, expense_category)
    return expense_input

def exportExpensesToCSV(table, filename):
    while True:
        # prompt user if they want the table to be saved
        user_input = input("Would you like to save this table on a .CSV file? (Y/N): ").lower()
        if user_input[0] == 'y':
            # save the table
            csv_file = f"tables\{filename}.csv"
            with open(csv_file, 'w') as f:
                f.write('expense_id, amount, reason, date, category_id\n')
                for data in table:
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]} \n")
            print("Table saved")
            break

        elif user_input[0] == 'n':
            break

        else:
            print("Please enter with Y/N ")

def exportCategoriesToCSV(table, filename):
    while True:
        # prompt user if they want the table to be saved
        user_input = input("Would you like to save this table on a .CSV file? (Y/N): ").lower()
        if user_input[0] == 'y':
            # save the table
            csv_file = f"tables\{filename}.csv"
            with open(csv_file, 'w') as f:
                f.write('category_id, category, total_expenses\n')
                for data in table:
                    f.write(f"{data[0]}, {data[1]}, {data[2]} \n")
            print("Table saved")
            break

        elif user_input[0] == 'n':
            break

        else:
            print("Please enter with Y/N ")

if __name__ == "__main__":
    print(getExpenseInput())

