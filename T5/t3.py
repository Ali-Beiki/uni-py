transactions = []

def add_transaction():
    amount = float(input("Enter transaction amount: "))
    description = input("Enter transaction description: ")
    transactions.append({"amount": amount, "description": description})
    print("Transaction added successfully.")

def show_transactions():
    if not transactions:
        print("No transactions found.")
    else:
        print("\nTransaction List:")
        for idx, trans in enumerate(transactions, 1):
            print(f"{idx}. Amount: {trans['amount']}, Description: {trans['description']}")

def delete_transaction():
    show_transactions()
    if transactions:
        try:
            index = int(input("Enter transaction number to delete: ")) - 1
            if 0 <= index < len(transactions):
                deleted = transactions.pop(index)
                print(f"Transaction with amount {deleted['amount']} deleted.")
            else:
                print("Invalid transaction number.")
        except ValueError:
            print("Please enter a valid number.")

def edit_transaction():
    show_transactions()
    if transactions:
        try:
            index = int(input("Enter transaction number to edit: ")) - 1
            if 0 <= index < len(transactions):
                new_amount = float(input("Enter new amount: "))
                new_description = input("Enter new description: ")
                transactions[index] = {"amount": new_amount, "description": new_description}
                print("Transaction updated successfully.")
            else:
                print("Invalid transaction number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\nBank Transaction Menu:")
        print("1. Add new transaction")
        print("2. Show all transactions")
        print("3. Delete transaction")
        print("4. Edit transaction")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            edit_transaction()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()