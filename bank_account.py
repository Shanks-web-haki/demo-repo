class BankAccount:
    def __init__(self):
        self.balance = 0  # initialize balance to 0
        print("Welcome to the Bank Account System!")

    def get_amount(self, prompt):
        """Ask for an amount until a valid positive number is entered."""
        while True:
            try:
                amount = float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount

    def deposit(self):
        amount = self.get_amount("Enter amount to be deposited:  ")
        self.balance += amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = self.get_amount("Enter amount to be withdrawn:  ")
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient funds !")

    def display(self):
        print("\nNet Available Balance =", self.balance)


if __name__ == "__main__":
    account = BankAccount()

    while True:
        print("\n1. Deposit  2. Withdraw  3. Display balance  4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            account.deposit()
        elif choice == "2":
            account.withdraw()
        elif choice == "3":
            account.display()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")