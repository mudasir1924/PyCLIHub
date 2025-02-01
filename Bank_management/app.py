class Bank: 
    bankname = 'Federal Bank' 
    branch = 'Hyd, India'

    # Create account: Constructor
    def __init__(self, username, pan, address): 
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0  # Set initial balance to zero
        print(f'Hello {self.username}, congrats! Your account has been created successfully.')

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount} deposited successfully. Your updated balance is {self.balance}.')
        else:
            print('Invalid amount. Please enter a positive value.')

    # Withdraw
    def withdraw(self, amount): 
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f'{amount} withdrawn successfully. Your updated balance is {self.balance}.')
            else:
                print('Insufficient funds.')
        else:
            print('Invalid amount. Please enter a positive value.')

    # Mini-statement
    def mini_statement(self): 
        print(f'Your account balance is: {self.balance}')

# Static variables accessible throughout the class
print(f'Welcome to {Bank.bankname}, {Bank.branch}')
username = input('Enter your Name: ')
pan = input('Enter your PAN: ')
address = input('Enter your Address: ')

# Create account object
account = Bank(username, pan, address)

while True: 
    print('\nPlease select any option: ')
    print('1. Deposit\n2. Withdraw\n3. Mini Statement\n4. Exit\n')

    try:
        option = int(input('Enter your choice: '))
        if option == 1:
            # Deposit
            try:
                amount = float(input('Enter deposit amount: '))
                account.deposit(amount)
            except ValueError:
                print('Invalid input. Please enter a numeric value.')
        elif option == 2:
            # Withdraw
            try:
                amount = float(input('Enter withdrawal amount: '))
                account.withdraw(amount)
            except ValueError:
                print('Invalid input. Please enter a numeric value.')
        elif option == 3:
            # Mini-statement
            account.mini_statement()
        elif option == 4:
            # Exit
            print('Thanks for using Federal Bank. Have a great day!')
            break
        else:
            print('Invalid option. Please select a valid menu option.')
    except ValueError:
        print('Invalid input. Please enter a number.')
