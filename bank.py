class User:
    account_number_counter = 1001  # Starting account number
    all_accounts = {} 

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.addres = address
        self.accountType = account_type
        self.balance = 0
        self.account_number = User.account_number_counter
        self.transaction_history = []
        self.loan_count = 0
        User.all_accounts[self.account_number] = self
        User.account_number_counter += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Amount {amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            print(f"Amount {amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Available balance: {self.balance}")
        return self.balance
    
    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transaction history available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Loan taken: {amount}")
            print(f"Loan of {amount} granted. Loan count: {self.loan_count}")
        else:
            print("Loan limit reached. Cannot take more loans.")

    def transfer(self, amount, target_account_number):
        if amount <= 0:
            print("Invalid transfer amount.")
        elif self.balance < amount:
            print("Insufficient funds for transfer.")
        else:
            target_account = User.all_accounts.get(target_account_number)
            if not target_account:
                print("Account does not exist.")
            else:
                self.balance -= amount
                target_account.balance += amount
                self.transaction_history.append(f"Transferred: {amount} to account {target_account_number}")
                target_account.transaction_history.append(f"Received: {amount} from account {self.account_number}")
                print(f"Amount {amount} transferred to account {target_account_number} successfully.")
    


