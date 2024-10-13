class SavingsAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return f"SavingsAccount(Holder: {self.account_holder}, Balance: ${self.balance:.2f})"

    def __lt__(self, other):
        """Compare SavingsAccount objects based on account_holder's name."""
        return self.account_holder < other.account_holder


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        # Sort accounts by account_holder name
        sorted_accounts = sorted(self.accounts)
        return "\n".join(str(account) for account in sorted_accounts)

# Example of usage
if __name__ == "__main__":
    bank = Bank()
    bank.add_account(SavingsAccount("Alice", 2500))
    bank.add_account(SavingsAccount("David", 1500))
    bank.add_account(SavingsAccount("Charlie", 3000))
    
    print(bank)
