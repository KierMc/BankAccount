
class BankAccount:
    
    all_accounts = []

    def __init__(self, balance): 
        self.int_rate = .01
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient funds: Charging a $5 Fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print("Balance: "+ str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= 1 + self.int_rate
        return self




user1= BankAccount(100)
user2= BankAccount(500)


user1.deposit(50).deposit(100).deposit(125).withdraw(175).yield_interest().display_account_info()
user2.deposit(200).deposit(300).withdraw(500).withdraw(200).withdraw(500).withdraw(195).yield_interest().display_account_info()