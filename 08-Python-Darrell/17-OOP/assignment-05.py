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

class BankAccount:
    def __init__(self, acct_id, acct_holderName):
        self.acct_id = acct_id
        self.acct_holderName = acct_holderName
        self.balance = 0
    
    def deposit(self, money):
        if money < 0 :
            print("Cannot deposit negative amount")
        else: 
            self.balance += money
            print(f"Deposited {money} into account {self.acct_id}")
    
    def withdraw(self, money):
        if money < 0 :
            print("Cannot withdraw negative amount")
        else:
            self.balance -= money
            print(f"Withdrew {money} from account {self.acct_id}")
    
    def GetBalance(self):
        print(f"Account Name: {self.acct_holderName} Account ID: {self.acct_id} Balance: {self.balance}")

mock = BankAccount("12345", "Checking")

mock.deposit(200)
mock.withdraw(50)

mock.GetBalance()


##########Part 2###########

class BankAccount:
    def __init__(self, acctId, holderName):
        self.AcctId = acctId
        self.AcctHolderName = holderName
        self.balance = 0
        self.transactions = [] #transaction tracker

    def deposit(self, amount):
        if amount < 0 :
            # raise an exception
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount    
        self.transactions.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if amount < 0 :
            # raise an exception
            raise ValueError("Withdrawal amount cannot be negative")
        # ensure there is sufficient balance to perform withdrawl
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal")
        """ 
        if insufficentBalance:
            # raise an exception
            pass 
        """
        self.balance -= amount
        self.transactions.append(f"Deposit: -{amount}")
        
    def getBalance(self):
        print(f"Account Name: {self.AcctHolderName} Account ID: {self.AcctId} Balance: {self.balance}")
    
    def transactionHistory(self):
        #return all the transactions
        return self.transactions



def main():
    mock = BankAccount("12345", "Checking")

    while True:
        print("Menu:")
        print("What operation would you like to do:")
        print("1. Deposit an amount into your account")
        print("2. Withdraw an amount from your account")
        print("3. Retrieve current balance")
        print("4. See previous transactions")
        print("5. Close Application")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit




mock.deposit(200)
mock.withdraw(50)
mock.deposit(5)

transactions = mock.transactionHistory()

for transaction in transactions:
    print(transaction)

print(mock.getBalance())