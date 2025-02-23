# Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details
monthly_installments = []  # Monthly installment logs

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03


def find_account_index(account_name):
    """Helper function to find account index."""
    if account_name in account_holders:
        return account_holders.index(account_name)
    else:
        return None


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
    print("1️1️ Identify Credit Card Type")
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

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            return "❌ Deposit amount must be greater than zero."

        balances[index] += amount
        transaction_histories[index].append(f"Deposited ${amount:.2f}")
        return f"✅${amount:.2f} was deposited successfully. New balance: ${balances[index]:.2f}"
    except ValueError:
        return "❌ Invalid amount! Please enter a valid number."


def withdraw():
    """Withdraw money from an account."""
    account_name = input("Enter the account holder's name: ")

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            return "❌ Withdraw amount must be greater than zero."

        if balances[index] < amount:
            return "❌ Insufficient balance!"

        balances[index] -= amount
        transaction_histories[index].append(f"Withdrawn ${amount:.2f}")
        return f"✅${amount:.2f} was withdrawn successfully. New balance: ${balances[index]:.2f}"
    except ValueError:
        return "❌ Invalid amount! Please enter a valid number."


def check_balance():
    """Check balance of an account."""
    account_name = input("Enter the account holder's name: ")

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    return f"{account_name}'s account balance is: ${balances[index]:.2f}"


def list_accounts():
    """List all account holders and details."""
    if not account_holders:
        return "There aren't any registered accounts at the moment!"
    else:
        return account_holders


def transfer_funds():
    """Transfer funds between two accounts."""
    account_name = input("Enter the account holder's name: ")

    index1 = find_account_index(account_name)

    if index1 is None:
        return "❌ Account not found."

    recipient_account_name = input("Enter the recipient's account name: ")

    index2 = find_account_index(recipient_account_name)

    if index2 is None:
        return "❌ Recipient account not found."

    try:
        amount = float(input("Enter the amount of transfer: "))
        if amount <= 0:
            return "❌ Transfer amount must be greater than zero."

        if balances[index1] < amount:
            return "❌ Insufficient balance!"

        balances[index1] -= amount
        transaction_histories[index1].append(f"Transferred ${amount:.2f}")
        balances[index2] += amount
        transaction_histories[index2].append(f"Received ${amount:.2f}")

        return f"✅${amount:.2f} was transferred successfully to {recipient_account_name}. New balance: ${balances[index1]:.2f}"

    except ValueError:
        return "❌ Invalid amount! Please enter a valid number."


def view_transaction_history():
    """View transactions for an account."""
    account_name = input("Enter the account holder's name: ")

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    return transaction_histories[index]


def apply_for_loan():
    """Allow user to apply for a loan."""
    account_name = input("Enter the account holder's name: ")

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    try:
        amount_of_loan = float(input("Enter amount of loan you want: "))

        if 0 < amount_of_loan <= MAX_LOAN_AMOUNT:
            months_to_repay_the_loan = int(
                input("Enter the repayment period in months (24 months is the maximum period): "))

            if 1 <= months_to_repay_the_loan <= 24:
                total_amount_to_repay = amount_of_loan * (1 + INTEREST_RATE)
                monthly_installment = total_amount_to_repay / months_to_repay_the_loan

                loans[index] = total_amount_to_repay
                monthly_installments[index] = monthly_installment

                while len(loan_history) <= index:
                    loan_history.append([])

                loan_history[index].append(f"Loaned ${amount_of_loan:.2f}")

                return f"✅ The loan of ${amount_of_loan:.2f} was approved successfully!\n" \
                       f"The total amount you will need to repay for the loan is: ${total_amount_to_repay:.2f}\n" \
                       f"The minimum monthly installment is: ${monthly_installments[index]:.2f}"
            else:
                return "❌ The repayment period should be 24 months or less."
        else:
            return f"❌ The loan amount must be greater than 0 and no more than ${MAX_LOAN_AMOUNT}."
    except ValueError:
        return "❌ Invalid amount! Please enter a valid number."


def repay_loan():
    """Allow user to repay a loan."""
    account_name = input("Enter the account holder's name: ")

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    if loans[index] == 0:
        return "❌ No active loan found for this account."

    try:
        amount_of_installment = float(input("Enter amount of monthly installment: "))

        if amount_of_installment < monthly_installments[index]:
            return f"❌ Deposit amount must be the same or greater than ${monthly_installments[index]:.2f}."

        if amount_of_installment > loans[index]:
            refund = amount_of_installment - loans[index]
            loans[index] = 0
            monthly_installments[index] = 0
            return f"🔄 Overpayment detected! Returning ${refund:.2f} to your account. Loan fully repaid!"

        loans[index] -= amount_of_installment
        loan_history[index].append(f"Repaid ${amount_of_installment:.2f}")

        if loans[index] <= 0:
            monthly_installments[index] = 0
            loans[index] = 0
            return "🎉 Loan fully repaid!"

        return f"✅ ${amount_of_installment:.2f} was withdrawn successfully. New balance: ${loans[index]:.2f}"

    except ValueError:
        return "❌ Invalid amount! Please enter a valid number."


def check_loan_status():
    """Check loan status for an account."""
    account_name = input("Enter the account holder's name: ")

    index = find_account_index(account_name)

    if index is None:
        return "❌ Account not found."

    if loans[index] == 0:
        return "❌ No active loan found for this account."

    return f"Loan Status for {account_name}:\n" \
           f"Total Loan: ${loans[index]:.2f}\n" \
           f"Remaining Loan: ${loans[index]:.2f}\n" \
           f"Monthly Installment: ${monthly_installments[index]:.2f}\n" \
           f"Loan History: {loan_history[index]}"


def identify_card_type():
    """Identify type of credit card."""
    card_number = input("Enter card number: ").replace(" ", "")
    length = len(card_number)

    if length not in [13, 15, 16, 19]:
        return "❌ Invalid card number length!"

    if card_number[0] == '4':
        if length == 13 or length == 16 or length == 19:
            return "Visa"

    if length == 16:
        for i in range(51, 56):
            if card_number[:2] == str(i):
                return "MasterCard"

        for j in range(2221, 2721):
            if card_number[:4] == str(j):
                return "MasterCard"

    if length == 15:
        if card_number[:2] in ['34', '37']:
            return "American Express"

    if length == 16:
        if card_number[:4] == '6011':
            return "Discover"

    return "❌ The card type cannot be recognized!"


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
            print(create_account())
        elif choice == 2:
            print(deposit())
        elif choice == 3:
            print(withdraw())
        elif choice == 4:
            print(check_balance())
        elif choice == 5:
            print(list_accounts())
        elif choice == 6:
            print(transfer_funds())
        elif choice == 7:
            print(view_transaction_history())
        elif choice == 8:
            print(apply_for_loan())
        elif choice == 9:
            print(repay_loan())
        elif choice == 10:
            print(check_loan_status())
        elif choice == 11:
            print(identify_card_type())
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
