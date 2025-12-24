import json
import os

DATA_FILE = "account.json"
account = None


def menu():
    print("\n1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. View transactions")
    print("6. Exit")


def load_account():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return None


def save_account(account):
    with open(DATA_FILE, "w") as f:
        json.dump(account, f)


def create_account():
    global account

    if account is not None:
        print("Account already exists.")
        return

    name = input("Enter account holder name: ")

    account = {
        "name": name,
        "balance": 0,
        "transactions": []
    }

    save_account(account)
    print("Account created successfully.")


def deposit_money():
    global account

    if account is None:
        print("Please create an account first.")
        return

    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount.")
        return

    account["balance"] += amount
    account["transactions"].append({
        "type": "Deposit",
        "amount": amount
    })

    save_account(account)
    print(f"Deposited ${amount}. New balance: ${account['balance']}")


def withdraw_money():
    global account

    if account is None:
        print("Please create an account first.")
        return

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount.")
        return

    if amount > account["balance"]:
        print("Insufficient balance.")
        return

    account["balance"] -= amount
    account["transactions"].append({
        "type": "Withdraw",
        "amount": amount
    })

    save_account(account)
    print(f"Withdrawn ${amount}. Remaining balance: ${account['balance']}")


def check_balance():
    if account is None:
        print("Please create an account first.")
        return

    print(f"Current balance: ${account['balance']}")


def transaction_history():
    if account is None:
        print("Please create an account first.")
        return

    if len(account["transactions"]) == 0:
        print("No transactions found.")
        return

    print("\n--- Transaction History ---")
    for i, tx in enumerate(account["transactions"], start=1):
        print(f"{i}. {tx['type']} - ${tx['amount']}")


account = load_account()

while True:
    menu()
    choice = input("Enter option: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        transaction_history()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
