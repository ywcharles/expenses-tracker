'''
 file: expense.py
 purpose: create expense class
 author: Charles Wu
'''

# imports
from datetime import date


class Expense:
    def __init__(self, amount, reason, category):
        self.__amount = amount
        self.__reason = reason
        self.__date = str((date.today()))
        self.__category = category.lower()

    # overloaders
    def __str__(self):
        return f"${self.getAmount():.2f} spent for {self.getReason()} on {self.getDate()}"

    # getters
    def getAmount(self):
        return self.__amount

    def getReason(self):
        return self.__reason

    def getDate(self):
        return self.__date

    def getCategory(self):
        return self.__category

    # setters
    def setCategory(self, new_category):
        self.__category = new_category
