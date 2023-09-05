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

def get_all_transactions():
    select_stmt = select(Transaction)
    return list(session.scalars(select_stmt))

def save_transactions(self):
    