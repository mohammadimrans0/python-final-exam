class User:
    account_number_counter = 1001
    user_accounts = {}
    total_loan_given = 0

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = User.account_number_counter
        self.transaction_history = []
        self.loan_count = 0
        User.user_accounts[self.account_number] = self
        User.account_number_counter += 1

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Amount {amount} deposited successfully.")

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
        if not Admin.loan_feature_enabled:
            print("Loan feature is currently disabled.")
            return
        if self.loan_count < 2:
            self.balance += amount
            User.total_loan_given += amount
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
            target_account = User.user_accounts.get(target_account_number)
            if not target_account:
                print("Account does not exist.")
            else:
                self.balance -= amount
                target_account.balance += amount
                self.transaction_history.append(f"Transferred: {amount} to account {target_account_number}")
                target_account.transaction_history.append(f"Received: {amount} from account {self.account_number}")
                print(f"Amount {amount} transferred to account {target_account_number} successfully.")

class Admin:
    loan_feature_enabled = True
    admin_accounts = {}

    def __init__(self, name, email, address, designation):
        self.name = name
        self.email = email
        self.address = address
        self.designation = designation
        Admin.admin_accounts[email] = self

    @staticmethod
    def delete_account(account_number):
        account = User.user_accounts.pop(account_number, None)
        if account:
            print(f"Account {account_number} deleted successfully.")
        else:
            print("Account does not exist.")

    @staticmethod
    def show_all_user_accounts():
        if not User.user_accounts:
            print("No accounts available.")
        else:
            print("List of all user accounts:")
            print("Account Number\tName\tBalance\tAccount Type")
            for account_number, user in User.user_accounts.items():
                print(f"{account_number}\t{user.name}\t{user.balance}\t{user.account_type}")

    @staticmethod
    def check_total_bank_balance():
        total_balance = sum(user.balance for user in User.user_accounts.values())
        print(f"Total available balance in the bank: {total_balance}")

    @staticmethod
    def check_total_loan_amount():
        total_loan = User.total_loan_given
        print(f"Total loan amount in the bank: {total_loan}")

    @staticmethod
    def toggle_loan_feature():
        Admin.loan_feature_enabled = not Admin.loan_feature_enabled
        status = "enabled" if Admin.loan_feature_enabled else "disabled"
        print(f"Loan feature has been {status}.")
