print("WELCOME TO SHOES SHOPPING!!")
class Shoes:
    def __init__(self,brand,size,color):
        self.brand=brand 
        self.size=size 
        self.color=color 
    def buy(self):
        ques1=input("Which brand do you want: ").upper()
        ques2=int(input("What is your size: "))
        ques3=input("Which color do you want: ").upper()
        brand_list=["NIKE","ADIDAS","REEBOK","FILA"]
        size_list=[6,7,8,9]
        color_list=["RED","BLACK","BLUE","WHITE"]
        if ques1 in brand_list:
            for self.brand in brand_list:
                print(f"Yes that {self.brand} is avaible!")
                if ques2 in size_list:
                    for self.size in size_list:
                        print(f"This {self.size} is avaible")
                        if ques3 in color_list:
                            for self.color in color_list:
                                print(f"Yes this {self.color} is avaible")
                                return True
        else:
            exit()
person=Shoes("nike",8,"black")
person.buy()
print("THANK YOU FOR SHOPPING!!")

                