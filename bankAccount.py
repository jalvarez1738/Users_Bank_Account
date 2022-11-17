class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = .05, balance = 100): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        
    def display_account_info(self):
        self = self
    def yield_interest(self):
        self.balance = self.balance*1.05

checking = BankAccount()
savings = BankAccount(.05, 999)

checking.deposit(222)
print(checking.balance)

# withdraw(self, amount)
# display_account_info(self)
# yield_interest(self)