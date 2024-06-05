from datetime import datetime
import color
# this tells us the transaction type and the amount, either a withdrawal or a deposit
class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

# This class handles deposit, withdraw, balance, and transaction history operations.
class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{color.RED} Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount))
            print(f"{color.GREEN} ${amount} successfully withdrawn.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions


