import datetime
from functools import reduce
import time
import csv
import os

""" 
Create a BankAccount class 
    - state
        AcctId
        AcctHolderName
    - behaviors
        Deposit
            validation : money cannot be negative
        Withdraw
            validation : money cannot be negative
        GetBalance()
"""
class InvalidTransactionAmountException(Exception):
    pass

class InsufficientBalanceException(Exception):
    pass

class AccountTransaction:
    def __init__(self, account, type, amount, desc):
        self.date = datetime.date.today()
        self.account = account
        self.type = type
        self.amount = amount
        self.desc = desc
    
    def __repr__(self) -> str:
        return f"({self.type, self.amount, self.date, self.desc})"
        
        
class BankAccount:
    def __init__(self, acctId, holderName):
        self.AcctId = acctId
        self.AcctHolderName = holderName
        self.transactions = tuple()
        
    def deposit(self, amount, desc=""):
        if amount < 0 :
            raise InvalidTransactionAmountException()
        self.transactions += (AccountTransaction(self, "DEPOSIT", amount, desc),)
        self.save_transactions()
        
    def withdraw(self, amount, desc=""):
        if amount < 0 :
           raise InvalidTransactionAmountException()
        # ensure there is sufficient balance to perform withdrawl
        if self.getBalance() - amount < 0:
            raise InsufficientBalanceException()
        self.save_transactions()
        
        self.transactions += (AccountTransaction(self, "WITHDRAW", amount, desc),)
        
    def getBalance(self):
        # account transaction as a tuple (type, amount)
        """ 
        return reduce(
            lambda result, txn : (result + txn[1]) if txn[0] == "DEPOSIT" else (result - txn[1]), 
            self.transactions, 
            0
        ) 
        """
        """ 
        result = 0
        for txn in self.transactions:
            if txn[0] == "DEPOSIT":
                result += txn[1]
            else:
                result -= txn[1]
        return result 
        """
        # using the AccountTransaction as a class
        """ 
        result = 0
        for txn in self.transactions:
            if txn.type == "DEPOSIT":
                result += txn.amount
            else:
                result -= txn.amount
        return result  
        """
        return reduce(
            lambda result, txn : (result + txn.amount) if txn.type == "DEPOSIT" else (result - txn.amount), 
            self.transactions, 
            0
        ) 
    def transactionHistory(self):
        return self.transactions
    
    def save_transactions(self):
        filename = f"{self.AcctHolderName}_transactions.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for transaction in self.transactions:
                writer.writerow([transaction.date,transaction.type, transaction.amount, transaction.desc])

    def load_transactions(self):
        filename = f"{self.AcctHolderName}_transactions.csv"
        transactions = []
        if os.path.exists(filename):
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        return transactions
    

if (__name__ == "__main__"):
    acct = BankAccount("Acct-101", "Magesh")
    acct.deposit(1000)
    try:
        acct.withdraw(500)
    except InsufficientBalanceException:
        print("You are attempting to withdraw more than the balance")
    
    try:  
        acct.withdraw(250)
    except InsufficientBalanceException:
        print("You are attempting to withdraw more than the balance")
        
    print(acct.transactionHistory())
    print(acct.getBalance())
    