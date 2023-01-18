print("Welcome to shoes shop")
class Owner:
    def __init__(self,shoes):
        self.shoes=shoes
    def display(self):
        print("These are my  branded shoes",self.shoes)
    def sell(self):
        for user in self.shoes:
            user=input("Which shoe do you want:")
            if user in self.shoes:
                self.shoes.remove(user)
                print("These brand shoes are still available",self.shoes)
                break
    def returnofshoe(self):
        user=input("Do you want to return this shoes:")
        if user=="yes":
            user=input("Which brand shoe it is: ")
            self.shoes.append(user)
            print(self.shoes)
class Customer:
    def __init__(self,shoes):
        self.shoes=shoes
    def purchase(self):
        user=input("Which brand shoe would you like to purchase:")
        if user in self.shoes:
            print("Your chice is great regardong the",user,"shoes")
            self.shoes.remove(user)
            print(self.shoes)
    def returnshoe(self):
        user=input("Which shoe do you want to return: ")
        if user in self.shoes:
            print("Are you sure , you want to return it: ",user)
            if user=="yes":
                print("Thank you. Please do visit again..")
                self.shoes.append(user)
                print(self.shoes)

obj1=Owner(["ADIDAS","NIKE","VANS"])
obj1.purchase()
obj1.returnshoe()
obj2=Customer(["ADIDAS","NIKE","VANS"])
obj2.purchase()
obj2.returnshoe()