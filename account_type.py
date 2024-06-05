from bank_account import BankAccount, Transaction
import color

# the savings account and current account is a child class to the BankAccount class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number):
        super().__init__(account_holder, account_number)
        self.interest_rate = 0.02
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


# here the user has access to an overdraft during withdrawal
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, account_number):
        super().__init__(account_holder, account_number)
        self.overdraft_limit = 1000.00
       
    
    def withdraw(self, amount):
        if amount <= self.balance:
            # using the principle of inheritance to use the withdraw method in the parent class, thus avoiding duplicate codes
            super().withdraw(amount)
            
        elif self.balance < amount <= self.balance + self.overdraft_limit:
        # Withdrawal amount exceeds balance but is within overdraft limit
            question = input(f"{color.YELLOW} Insufficient funds. Do you want to use overdraft? (y/n): {color.RESET} ").lower()
            if question.lower() == 'y':
                # User agrees to use overdraft
                remaining_amount = amount - self.balance
                self.balance = 0
                self.overdraft_limit -= remaining_amount
                self.transactions.append(Transaction("Overdraft Withdrawal",  amount))
                print(f"{color.GREEN} Withdrawal successful. You have used overdraft.")

            elif question.lower() == 'n':
                # User declines to use overdraft
                print(f"{color.RED} Withdrawal canceled due to insufficient funds.")

            else:
                # Invalid response
                print(f"{color.RED} Invalid response! Withdrawal canceled.")
        else:
            # Withdrawal amount exceeds available balance and overdraft limit
            print(f"{color.RED} Sorry, you do not have sufficient funds and you have exceeded your overdraft limit.")


    def get_overdraft_limit(self):
        return self.overdraft_limit