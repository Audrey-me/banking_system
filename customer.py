import color

# this is a customer class that can have one or multiple accounts
class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = [] # a list to store account

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts
