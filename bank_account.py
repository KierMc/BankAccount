
class BankAccount:
    
    accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

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

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()



user1= BankAccount(.01, 100)
user2= BankAccount(.05, 500)


user1.deposit(50).deposit(100).deposit(125).withdraw(175).yield_interest().display_account_info()
user2.deposit(200).deposit(300).withdraw(500).withdraw(200).withdraw(500).withdraw(195).yield_interest().display_account_info()

BankAccount.print_all_accounts()