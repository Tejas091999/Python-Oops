print("Cricket batsman selection")
class Cricket():
    def __init__(self,name,age,s_rate):
        self.name=name 
        self.age=age 
        self.s_rate=s_rate 
    def player(self):
        while True:
            self.name=input("What is your name: ")
            self.age=int(input("What is your age: "))
            matches=int(input("How many matches played: "))
            runs=int(input("How many runs: ")) 
            self.s_rate=(runs/matches)
            print(self.s_rate)
            names=[]
            if self.age>18 and self.s_rate>30:
                names.append(self.name)
                print(self.name,"you're selected")
                print(names)
                continue
            else:
                 print("You're under age.Please try after some years")
                 print("Thank you")
                 break
print("Thank you!!")
person=Cricket("tejas",12,34)
person.player()

