import random
print("WELCOME TO MUSIC PLAYER")
class Artist():
    def __init__(self,name,genre):
        self.name=name 
        self.genre=genre 
    def user(self):
        self.name=input("Which artist do you want to hear: ")
        print(f"{self.name},You've choosen a great artist.")
        self.genre=input("Of which genere do you want to hear: ").lower()
        print(f"Playing {self.genre} songs for you!")
        happy_list=["Let's Go Crazy by Prince","Good as Hell","Lovely Day"]
        sad_list=["Hurt","Teardrop","The Boxer","No Name"]
        lofi_list=["Take Me. Miso. Miso","Falling for U","Fool. Cavetown"]
        person=input("Do you want to shuffle the playlist: ").lower()
        if self.genre=="happy" and person=="yes":
            songs=random.choice(happy_list)
            print(songs)
        elif self.genre=="sad" and person=="yes":
            songs=random.choice(sad_list)
            print(songs)
        elif self.genre=="lofi" and person=="yes":
            songs=random.choice(lofi_list)
            print(songs)
obj=Artist("name","genre")
person1=obj.user()
print(person1)