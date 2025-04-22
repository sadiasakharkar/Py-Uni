class BankAccount:
    def __init__(self, account_number, balance=1000):
        """Constructor initializes account number and balance with conditions."""
        self.account_number = account_number
        self.balance = max(balance, 100)  # Ensures the minimum balance is 100

    def display_details(self):
        """Displays account details."""
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

# Creating two BankAccount objects with different initial balances
account1 = BankAccount("A12345", 1500)  # Balance remains 1500
account2 = BankAccount("B67890", 50)    # Balance is set to minimum 100

# Displaying account details
account1.display_details()
print("\n")
account2.display_details()
