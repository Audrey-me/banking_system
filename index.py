import bank
import color

def main():
    bank_system = bank.Bank()  # Create an instance of the Bank class

    while True:
        print("\nChoose an option:")
        print("a. Create a customer")
        print("b. Create an account")
        print("c. Deposit money")
        print("d. Withdraw money")
        print("e. List all accounts")
        print("f. Check balance")
        print("g. Delete an account")
        print("h. Transfer money")
        print("i. Quit")

        option = input(f"{color.YELLOW} Enter your option: {color.RESET} ").lower()

        if option == 'a':
            name = input(f"{color.YELLOW} Enter customer name: {color.RESET} ")
            customer = bank_system.get_customer(name)
            if customer:
                print("Customer already exists. Choose an account to operate on:")
                for i, account in enumerate(customer.accounts):
                    print(f"{i+1}. Account Number: {account.account_number}, Account Type: {account.__class__.__name__}")
                account_index = int(input(f"{color.YELLOW} Enter account number to operate on: {color.RESET} ")) - 1
                selected_account = customer.accounts[account_index]
                # Proceed with further operations on the selected account
            else:
                bank_system.create_customer(name)

        elif option == 'b':
            account_type = input(f"{color.YELLOW} Enter account type (savings or current): {color.RESET} ")
            bank_system.create_account(name, account_type)

        elif option == 'c':
            account_number = input(f"{color.YELLOW} Enter account number: {color.RESET}")
            amount = float(input(f"{color.YELLOW}Enter amount to deposit: {color.RESET} "))
            bank_system.deposit(account_number, amount)
        
        elif option == 'd':
            account_number = input(f"{color.YELLOW}Enter account number: {color.RESET} ")
            amount = float(input(f"{color.YELLOW} Enter amount to withdraw: {color.RESET} "))
            bank_system.withdraw(account_number, amount)
        
        elif option == 'e':
            bank_system.list_all_accounts()
        
        elif option == 'f':
            account_number = input(f"{color.YELLOW} Enter account number:{color.RESET} ")
            balance = bank_system.check_balance(account_number)
            print(f"Account Balance: {balance}")
        
        elif option == 'g':
            account_number = input(f"{color.YELLOW} Enter account number: {color.RESET} ")
            bank_system.delete_account(account_number)
        
        elif option == 'h':
            from_account_number = input(f"{color.YELLOW} Enter your account number: {color.RESET}")
            to_account_number = input(f"{color.YELLOW} Enter the account number to transfer to: {color.RESET} ")
            amount = float(input(f"{color.YELLOW} Enter amount to transfer: {color.RESET}"))
            bank_system.transfer(from_account_number, to_account_number, amount)
        
        elif option == 'i':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
