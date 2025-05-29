class Account:
    def __init__(self, initial_balance):
        # بررسی اینکه موجودی اولیه منفی نباشد
        if initial_balance >= 0:
            self.balance = initial_balance
        else:
            raise ValueError("Initial balance cannot be negative")

    def credit(self, amount):
        # اطمینان از مثبت بودن مقدار واریز
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Credit amount must be positive")

    def debit(self, amount):
        # بررسی مقدار برداشت و موجودی کافی
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError("Insufficient balance for withdrawal")
        else:
            raise ValueError("Debit amount must be positive")

    def getBalance(self):
        # برگرداندن موجودی فعلی
        return self.balance

# Interactive menu with while loop
if __name__ == "__main__":
    # ایجاد حساب با موجودی اولیه 1000
    account = Account(1000)
    print(f"Initial Balance: {account.getBalance()}")

    while True:
        print("\nOptions:")
        print("1. Credit")
        print("2. Debit")
        print("3. Get Balance")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")

        if choice == "1":
            try:
                amount = float(input("Enter credit amount: "))
                account.credit(amount)
                print(f"New Balance: {account.getBalance()}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                amount = float(input("Enter debit amount: "))
                account.debit(amount)
                print(f"New Balance: {account.getBalance()}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            print(f"Current Balance: {account.getBalance()}")

        elif choice == "4":
            print("Exiting program. Final Balance:", account.getBalance())
            break

        else:
            print("Invalid option! Please try again.")