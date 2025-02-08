# Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details
loan_history = [] # Account loan logs


MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Check Loan Status")
    print("1️1️ View Loan History")
    print("1️2️ Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account():
    """Create a new account."""
    account_name = input("Enter the account holder's name: ")
    account_holders.append(account_name)
    balances.append(0)
    transaction_histories.append([])
    loans.append(0)

    return f"Account for {account_name} was created successfully with a balance of $0.00 and 0 loans"


def deposit():
    """Deposit money into an account."""
    account_name = input("Enter the account holder's name: ")

    if account_name in account_holders:
        index = account_holders.index(account_name)
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("❌ Deposit amount must be greater than zero.")
                return

            balances[index] += amount
            transaction_histories[index].append(f"Deposited ${amount:.2f}")
            print(f"✅${amount:.2f} was deposited successfully. New balance: ${balances[index]:.2f}")
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")
    else:
        print("❌ Account not found.")


def withdraw():
    """Withdraw money from an account."""
    account_name = input("Enter the account holder's name: ")

    if account_name in account_holders:
        index = account_holders.index(account_name)
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("❌ Deposit amount must be greater than zero.")
                return

            balances[index] -= amount
            transaction_histories[index].append(f"Withdrawn ${amount:.2f}")
            print(f"✅${amount:.2f} was withdrawn successfully. New balance: ${balances[index]:.2f}")
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")
    else:
        print("❌ Account not found.")


def check_balance():
    """Check balance of an account."""
    account_name = input("Enter the account holder's name: ") #Ima error

    if account_name in account_holders:
        index = account_holders.index(account_name)
        print(f"{account_name}'s account balance is: ${balances[index]:.2f}")
    else:
        print("❌ Account not found.")


def list_accounts():
    """List all account holders and details."""
    if not account_holders:
        print("There aren't any registered accounts at the moment!")
    else:
        print(account_holders)


def transfer_funds():
    """Transfer funds between two accounts."""
    account_name = input("Enter the account holder's name: ")
    if account_name in account_holders:
        index1 = account_holders.index(account_name)
        recipient_account_name = input("Enter the recipient's account name: ")
        if recipient_account_name in account_holders:
            index2 = account_holders.index(recipient_account_name)
            try:
                amount = float(input("Enter the amount of transfer: "))
                if amount <= 0:
                    print("❌ Deposit amount must be greater than zero.")
                    return

                balances[index1] -= amount
                transaction_histories[index1].append(f"Transferred ${amount:.2f}")
                print(f"✅${amount:.2f} was transferred successfully to {recipient_account_name}. New balance: ${balances[index1]:.2f}")

                balances[index2] += amount
                transaction_histories[index2].append(f"Received ${amount:.2f}")
            except ValueError:
                print("❌ Invalid amount! Please enter a valid number.")
        else:
            print("❌ Account not found.")
    else:
        print("❌ Account not found.")


def view_transaction_history():
    """View transactions for an account."""
    account_name = input("Enter the account holder's name: ")

    if account_name in account_holders:
        index = account_holders.index(account_name)
        print(transaction_histories[index])
    else:
        print("❌ Account not found.")


def apply_for_loan():
    """Allow user to apply for a loan."""
    account_name = input("Enter the account holder's name: ")

    if account_name in account_holders:
        index = account_holders.index(account_name)
        try:
            amount_of_loan = float(input("Enter amount of loan you want: "))

            if 0 < amount_of_loan <= MAX_LOAN_AMOUNT:
                months_to_repay_the_loan = int(
                    input("Enter the repayment period in months(24 months is the maximum period): "))

                if months_to_repay_the_loan <= 24:
                    total_amount_to_repay = amount_of_loan * (1 + INTEREST_RATE)
                    monthly_installment = total_amount_to_repay / months_to_repay_the_loan

                    loans[index] = total_amount_to_repay

                    while len(loan_history) <= index:
                        loan_history.append([])

                    loan_history[index].append(f"Loaned ${amount_of_loan:.2f}")

                    print(f"✅ The loan of ${amount_of_loan:.2f} was approved successfully!")
                    print(f"The total amount you will need to repay for the loan is: ${total_amount_to_repay:.2f}")
                    print(f"The minimum monthly installment is: ${monthly_installment:.2f}")
                else:
                    print("❌ The repayment period should be 24 months or less.")
            else:
                print(f"❌ The loan amount must be greater than 0 and no more than ${MAX_LOAN_AMOUNT}.")
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")
    else:
        print("❌ Account not found.")


def repay_loan():
    """Allow user to repay a loan."""
    pass


def check_loan_status():
    pass


def view_loan_history():
    account_name = input("Enter the account holder's name: ")

    if account_name in account_holders:
        index = account_holders.index(account_name)
        print(loan_history[index])
    else:
        print("❌ Account not found.")

def identify_card_type():
    """Identify type of credit card."""
    pass


def main():
    """Run the banking system."""
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            check_loan_status()
        elif choice == 11:
            view_loan_history()
        elif choice == 12:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
