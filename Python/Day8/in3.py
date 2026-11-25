
# Base class
class Account:
    def get_interest_rate(self):
        return 4

# First subclass
class SavingsAccount(Account):
    def get_interest_rate(self):
        return 5

# Second subclass
class FixedDeposit(Account):
    def get_interest_rate(self):
        return 7

# Creating objects
a1 = Account()
a2 = SavingsAccount()
a3 = FixedDeposit()

# Storing objects in a list
accounts = [a1, a2, a3]

# Calling method using loop
for account in accounts:
    print("Interest Rate:", account.get_interest_rate(), "%")
