print("WELCOME TO MOVIE BOOKINGS!!")
while True:
    name = input("Enter your name: ")
    movies = ["BLACK PANTHER","IRON MAN 3","SUPERMAN","BATMAN"]
    name_of_movie= input("Which movie would like to watch: ").upper()
    seats = 100
    if name_of_movie in movies:
        print("There's a show!!")
        age = int(input("What is your age: "))
        if age > 18:
            number_of_seats = int(input("How many number of seats do you want to book: "))
            if number_of_seats > seats:
                print("There are NO more seats avaible!")
            else:
                print("You're booking is done!")
                remaining_seats = seats - number_of_seats
                print(f"There are {remaining_seats} seats remaining")
                break
        else:
            print("You're under age!")
            break
    else:
        print("There are no shows!!")
        break
print("Thank you for your time.")
print("Please do visit again!")

