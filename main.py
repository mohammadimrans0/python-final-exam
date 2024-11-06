from bank import *

def user_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    account_type = input("Enter Account Type (Savings/Current): ")
    user = User(name=name, email=email, address=address, account_type=account_type)
    
    while True:
        print(f"\nWelcome {user.name}!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Amount")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            amount = int(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == 3:
            user.check_balance()
        elif choice == 4:
            user.show_transaction_history()
        elif choice == 5:
            if Admin.loan_feature_enabled:
                amount = float(input("Enter loan amount: "))
                user.take_loan(amount)
            else:
                print("Loan feature is currently disabled.")
        elif choice == 6:
            target_account = int(input("Enter target account number: "))
            amount = float(input("Enter amount to transfer: "))
            user.transfer(amount, target_account)
        elif choice == 7:
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    designation = input("Enter Your Designation : ")
    admin = Admin(name=name, email=email, address=address, designation=designation)
  
    while True:
        print(f"\nWelcome {admin.name}!")
        print("1. Create New User Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            user_name = input("Enter User Name: ")
            user_email = input("Enter User Email: ")
            user_address = input("Enter User Address: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            new_account = User(name=user_name, email=user_email, address=user_address, account_type=account_type)
            print(f"Account created successfully with Account Number: {new_account.account_number}")
        elif choice == 2:
            account_number = int(input("Enter Account Number to delete: "))
            admin.delete_account(account_number)
        elif choice == 3:
            admin.show_all_user_accounts()
        elif choice == 4:
            admin.check_total_bank_balance()
        elif choice == 5:
            admin.check_total_loan_amount()
        elif choice == 6:
            admin.toggle_loan_feature()
        elif choice == 7:
            break
        else:
            print("Invalid Input")

while True:
    print("\nWelcome to the Bank Management System!")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        user_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")
