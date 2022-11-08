class Budget():
    def __init__(self,balance):
        self.balance = balance
    def food(self):
        user = int(input("How much do you want to spend on food: "))
        if user > self.balance:
            print("Sorry!! You don't have enough balance")
            user = input("Do you want to deposit:")
            if user == "yes":
                deposit = int(input("how much amount would you like to deposit on food: "))
                self.balance = self.balance + deposit
                return self.balance
            else:
                return self.balance
        elif user < self.balance:
            withdraw = self.balance - user
            return withdraw
    def clothing(self):
        user = int(input("How much do you want to spend on clothing: "))
        if user > self.balance:
            print("Sorry!! You don't have enough balance")
            user = input("Do you want to deposit:")
            if user == "yes":
                deposit = int(input("how much amount would you like to deposit on clothing: "))
                self.balance = self.balance + deposit
                return self.balance
            else:
                return self.balance
        elif user < self.balance:
            withdraw = self.balance - user
            return withdraw
    def shelter(self):
        user = int(input("How much do you want to spend on shelter: "))
        if user > self.balance:
            print("Sorry!! You don't have enough balance")
            user = input("Do you want to deposit:")
            if user == "yes":
                deposit = int(input("how much amount would you like to deposit on shelter: "))
                self.balance = self.balance + deposit
                return self.balance
            else:
                return self.balance
        elif user < self.balance:
            withdraw = self.balance - user
            return withdraw
person1=Budget(5000)
necessity_1 = person1.food()
necessity_2 = person1.clothing()
necessity_3 = person1.shelter()
total_balance = necessity_1 + necessity_2 + necessity_3
print(total_balance)

