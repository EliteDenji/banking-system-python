
accounts = {}

def generate_account_number():
    return str(len(accounts) + 1001)

# Create Account
def create_account():
    name = input("Enter Account Holder Name: ")

    while True:
        acc_type = input("Enter Account Type (Savings/Current): ").lower()
        
        if acc_type == "savings" or acc_type == "current":
            acc_type = acc_type.capitalize()  
            break
        else:
            print("❌ Invalid input! Please enter 'Savings' or 'Current'.")

    acc_no = generate_account_number()

    accounts[acc_no] = {
        "name": name,
        "type": acc_type,
        "balance": 0,
        "transactions": []
    }

    print("✅ Account created successfully!")
    print("Your Account Number is:", acc_no)
# Deposit Money
def deposit():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        accounts[acc_no]["transactions"].append(f"Deposited: {amount}")
        print("Deposit successful!")
    else:
        print("Account not found!")

# Withdraw Money
def withdraw():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            accounts[acc_no]["transactions"].append(f"Withdrawn: {amount}")
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

# Check Balance
def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Current Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!")

# Transaction History
def transaction_history():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Transaction History:")
        for t in accounts[acc_no]["transactions"]:
            print("-", t)
    else:
        print("Account not found!")

# Delete Account
def delete_account():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        del accounts[acc_no]
        print("Account deleted successfully!")
    else:
        print("Account not found!")

# Main Menu
def menu():
    while True:
        print("\n====== BANKING SYSTEM ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transaction_history()
        elif choice == '6':
            delete_account()
        elif choice == '7':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
menu()

