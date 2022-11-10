class Bike():
    def __init__(self,engine,color):
        self.engine = int(input("How many engine power do you want:"))
        self.color = input("Which color do you want: ")
    def engine_type(self):
        if self.engine > 150 :
            print("That's more power!")
        elif self.engine < 150 :
            print("You can handle the it.")
    def color_type(self):
        if self.color == "white":
            print("Please wash it")
        elif self.color == "black":
            print("Please avoid crashes")
        elif self.color == "red":
            print("It is the prettiest color")
        else:
            print("There is NO availble color")
class Rider(Bike):
    def __init__(self,age,license):
        self.age = int(input("Enter your age: "))
        self.license = input("Do you have license: ")
    def driver_check(self):
        if self.age >= 18 and self.license == "yes":
            print("You can drive the bike. Enjoy!!")
        elif self.age < 18 and self.license =="no":
            print("Sorry!! you are not eligible")
requirment1 = Bike(60,"black")
requirment2= Rider(19,"yes")
requirment2.driver_check()
requirment1.engine_type()
requirment1.color_type()

