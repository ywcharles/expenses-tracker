'''
    file: createDB.py
    purpose: create databases tables
    author: Charles Wu
'''

# imports
import mysql.connector

# open database
# PLEASE ENTER HOST, USER, PASSWORD AND DATABASE
expenses_db = mysql.connector.connect(
  host="***INSERT HOST HERE***",
  user="***INSERT USER HERE***",
  password="***INSERT PASSWORD HERE***",
  database="***INSERT DATABASE HERE***"
)

# create cursor
my_cursor = expenses_db.cursor()

# create table for customers
my_cursor.execute("CREATE TABLE expenses ("
                  "expense_id INT NOT NULL AUTO_INCREMENT,"
                  "amount DECIMAL(6,2),"
                  "reason VARCHAR(150),"
                  "expense_date DATE,"
                  "category_id INT,"
                  "PRIMARY KEY(expense_id)"
                  ");")

# create table for categories
my_cursor.execute("CREATE TABLE categories("
                  "category_id INT NOT NULL AUTO_INCREMENT,"
                  "category_name VARCHAR(150),"
                  "total_expenses DECIMAL(6,2),"
                  "PRIMARY KEY(category_id)"
                  ");")

# link expenses and categories
my_cursor.execute("ALTER TABLE expenses "
                  "ADD FOREIGN KEY(category_id) "
                  "REFERENCES categories(category_id) "
                  "ON DELETE CASCADE"
                  ";")

print("Table categories and expenses were created!")