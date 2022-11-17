from bankAccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdraw(self, amount):
        self.account.withdraw(amount)

    def transfer_money(self, amount, other_user)


john = User('John', 'jrock@gmail.com')
print(john.account.balance)