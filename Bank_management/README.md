# Federal Bank Console Banking System

Welcome to the **Federal Bank Console Banking System**! 
This is a simple Python-based banking system that allows users to create an account, deposit money, withdraw funds, and view their account balance (mini-statement) – all from the terminal.

## 🏦 Features

- **Account Creation:** Create an account with name, PAN, and address.
- **Deposit:** Deposit money into your account.
- **Withdraw:** Withdraw money with balance check.
- **Mini-Statement:** View your current account balance.
- **Error Handling:** Ensures valid transactions (positive amounts).

## 🛠️ How It Works

1. **Create an Account** with basic details (name, PAN, address).
2. **Deposit and Withdraw** funds.
3. **View Balance** via mini-statement.
4. **Exit** the system at any time.

---------------------------------------------------------------------------------------------------------------------

Sample Interaction:

Welcome to Federal Bank, Hyd, India
Enter your Name: John Doe
Enter your PAN: ABCDE1234F
Enter your Address: 123 Main St, Hyd

Hello John Doe, congrats! Your account has been created successfully.

Please select any option:
1. Deposit
2. Withdraw
3. Mini Statement
4. Exit

Enter your choice: 1
Enter deposit amount: 5000
5000.0 deposited successfully. Your updated balance is 5000.0.

---------------------------------------------------------------------------------------------------------------------

Code Structure:
Class Bank:
__init__: Initializes user account.
deposit: Handles deposits.
withdraw: Handles withdrawals.
mini_statement: Displays account balance.