
class Bank():
    def __init__(self,name,balance,account_number=1999):
        self.name = name
        self.balance = balance
        self.account_number = account_number
    def deposit(self,amount):
        self.balance = amount + self.balance
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("There is no enough balance")
        else:
            self.balance = self.balance - amount
            return self.balance
    def balance_in_bank(self):
        return self.balance
person1 = Bank("Tejas",30000)
print(person1.deposit(50000))
print(person1.balance_in_bank())
print(person1.withdraw(20000))