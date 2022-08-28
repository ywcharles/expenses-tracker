# expenses-tracker
The program has the purpose of tracking expenses inputted by the user. It utilizes a SQL database to store the data and it also allows the user to export the data into a .CSV file.  Ther program allows the user to display the data by category of the expense, all expenses, last week expesnses, monthly expenses and also by an inputted month and category.

Instructions:
  
  1. Install mySQL (https://dev.mysql.com/downloads/mysql/)
  2. Install mySQL module for python
  3. Open mySQL command line client on your desktop and log in
  4. Type `create database` + a database name by your choice and press enter
  5. Open `sqltools.py` and `createDB.py`
  6. Insert your SQL host, user, password and database name on `
  host="***INSERT HOST HERE***"`,
  `user="***INSERT USER HERE***"`,
  `password="***INSERT PASSWORD HERE***"`,
  `database="***INSERT DATABASE HERE***"` respectively
  7. Run the `createDB.py` file
  8. You are all set!!

How the program works:

  When you need to insert, check or delete data run the `main.py` file and choose one of the options:
  1. Insert expense ( insert an expense with it's amount, reason and category. If the category doesn't exist, it will be created automatically by the program)
  2. Display last week's expenses ( displays last week's expenses, and ask if user wants to export the data to a .csv file)
  3. Display expenses by month ( displays a inputted month's expenses, and ask if user wants to export the data to a .csv file)
  4. Display by category ( displays all the categories and it's total expenses, and ask if user wants to export the data to a .csv file)
  5. Display category's monthly expenses ( displays an inputted month and category's expenses, and ask if user wants to export the data to a .csv file)
  6. Display all expenses ( displays all expenses, and ask if user wants to export the data to a .csv file)
  7. Delete an input ( asks for an expense's ID and deletes the exepense with taht ID)
  8. Exit program ( exits program)
  
