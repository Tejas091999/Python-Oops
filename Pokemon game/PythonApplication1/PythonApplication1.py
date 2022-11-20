class Pokemon:
    def __init__(self,name,primary_type,power):
        self.name=name
        self.primary_type=primary_type 
        self.power=power
    def __str__(self):
        return f"{self.name}({self.primary_type}) : {self.power}"
    def feed(self):
        if self.power < 0:
            self.power=+1
            print(f"{self.name} has {self.power}")
        else:
            print(f"{self.name} has a great power {self.power} which is enough!!")
    def battle(self,other):
        print("Let's Battle:",self.name,other.name)
        result=self.typewheel(self.primary_type,other.primary_type)
        if result == "lose":
            self.power -= 10
            print(f"{self.name} lost and now has {self.power}.")
        print(f"{self.name} fought {other.name} and the result is {result}")
    staticmethod
    def typewheel(type1,type2):
        result={0:"lose",1:"win",-1:"tie"}
        game_map={"water":0,"fire":1,"grass":2}
        wl_matrix =[[-1,1,0],[0,-1,1],[1,0,-1]]
        game_map["water"]
        wl_matrix[0][1]
        wl_result=wl_matrix[game_map["type1"]],[game_map["type2"]]
        return result[wl_result]
if __name__=="__main__":
    print(Pokemon(name="bulbasaur",primary_type="grass",power=25))
    print(Pokemon(name="charmander",primary_type="fire",power=20))

        