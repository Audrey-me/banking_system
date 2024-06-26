# Banking System Project
This project is a practical hands-on exercise aimed at utilizing concepts related to Object Oriented Programming in python, and explains further the concept of classes and it's importance. 

## Project Structure

📂 **index.py**
 Handles user interaction and directs to appropriate actions.

📂 **customer.py**
 Defines the Customer class with an account list.

📂 **bank_account.py**
 Defines BankAccount and Transaction classes for basic account operations within a single account.

📂 **account_type.py(child classes)**
    Defines SavingsAccount and CurrentAccount classes inheriting from BankAccount.

📂 **bank.py**
    Defines the Bank class to manage customers and accounts, perform operations like deposit, withdrawal, transfer, and manage accounts.


## Steps to Follow
1. cd into the project folder:
   ```bash
   cd banking_system
   ```
2. Make the script executable by running the following command:
    ```bash
   chmod 700 index.py
   ```

3. Run the script using Python:
    ```bash
   python index.py
   ```


