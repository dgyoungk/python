#This module class bankaccount simulates a bank account

class BankAccount:

    #__init__ method works like a constructor
    #the __before an attribute make them private

    def __init__(self, bal):
        self.__balance = bal

    #class methods: deposit, withdrawal, show balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds")

    def get_balance(self):
        return self.__balance

    #toString method
    def __str__(self):
        return f"The balance is ${self.__balance:.2f}"
