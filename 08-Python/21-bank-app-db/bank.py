#custom exceptions

from datetime import date, datetime
from functools import reduce
import datetime
from sqlalchemy import DateTime, create_engine, select, Column, Integer, String
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column("transaction_id", Integer, primary_key=True)
    type = Column(String)
    amount = Column(Integer) 
    txn_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Transaction({self.id},'{self.type}','{self.amount}', {self.txn_date})"

    def __str__(self):
        return f"Transaction({self.id},'{self.type}','{self.amount}', {self.txn_date})"

engine = create_engine("sqlite:///./bank.sqlite", echo=True)

session = Session(engine)



class InvalidAmount(Exception):
    pass

class InsufficientBalance(Exception):
    pass



class BankAccount:
    def __init__(self, name, storage):
        self.name = name
        self._storage = storage
        self._transactions = storage.get_transactions()

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmount()
        else:
            transaction = ('Deposit', amount)
            self._storage.save_transaction(('Deposit', amount))
            self._transactions += ( transaction,)
            

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance()
        else:
            transaction = ('Withdraw', amount)
            self._storage.save_transaction(('Withdraw', amount))
            self._transactions += (transaction, )

    def history(self):
        return self._transactions

    @property
    def balance(self):
        #using the history to calc the balance!
        result = reduce(lambda result, txn: (result + int(txn[1]))  if txn[0] =='Deposit' else (result - int(txn[1])), self._transactions, 0)
        return result
    
