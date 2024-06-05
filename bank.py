from customer import Customer
from account_type import SavingsAccount, CurrentAccount
import color
import random

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def create_customer(self, name):
        if name in self.customers:
            print(f"{color.RED}The Customer {name} already exists.")
        else:
            self.customers[name] = Customer(name)
            print(f"{color.GREEN}Customer {name} created successfully")

    def get_customer(self, name):
        return self.customers.get(name, None)

    def generate_account_number(self):
        return str(random.randint(10000000, 99999999))

    def create_account(self, name, account_type):
        customer = self.get_customer(name)
        if not customer:
            print(f"{color.RED} Customer not found!!")
            return
        
        account_number = self.generate_account_number()
        if account_type == "savings":
            account = SavingsAccount(name, account_number)
        elif account_type == "current":
            account = CurrentAccount(name, account_number)
        else:
            print(f"{color.RED}Invalid account type")
            return
        
        customer.add_account(account)
        self.accounts[account_number] = account
        print(f"{color.GREEN}Account {account_number} of type {account_type} created successfully for {name}")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            print(f"{color.GREEN}Deposited {amount} to account {account_number}.")
        else:
            print(f"{color.RED}Account {account_number} not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            
        else:
            print(f"{color.RED}Account {account_number} not found.")

    def list_all_accounts(self):
        if not self.accounts:
            print(f"{color.YELLOW}No accounts found.")
            return

        for account_number, account in self.accounts.items():
            print(f"{color.GREEN} Account Number: {account_number}, Account Holder: {account.account_holder}, Balance: {account.get_balance()}, Account Type: {account.__class__.__name__}")


    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_balance()
        else:
            print(f"{color.RED}Account {account_number} not found.")
            return None

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"{color.GREEN}Account {account_number} deleted successfully.")
        else:
            print(f"{color.RED}Account {account_number} not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        
        if not from_account:
            print(f"{color.RED}From account {from_account_number} not found.")
            return
        
        if not to_account:
            print(f"{color.RED}To account {to_account_number} not found.")
            return

        if from_account.get_balance() < amount:
            print(f"{color.RED}Insufficient funds in from account.")
            return
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"{color.GREEN}Transferred {amount} from account {from_account_number} to account {to_account_number}.")
