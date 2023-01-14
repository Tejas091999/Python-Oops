print("Petrol Indicator")
cars=["HONDA","SANTRO","TIAGO","FORTUNER"]
user=input("Which car do you want to choose: ").upper()
petrol_price=90
if user in cars:
    print(user,"You have a great choice")
    if user=="HONDA":
        tank_size=35
        distance=int(input("How much kilometers you have to drive: "))
        pay=int(input("How much amount you're going to pay: "))
        petrol_filled=(pay/petrol_price)
        petrol_tank=tank_size-petrol_filled 
        print(petrol_tank)
        average=(petrol_tank/distance)
        print(average)
        if average>10:
            print("This car is suitable")
        else:
            print("Please choose another car.")
    if user=="SANTRO":
        tank_size=25
        distance=int(input("How much kilometers you have to drive: "))
        pay=int(input("How much amount you're going to pay: "))
        petrol_filled=(pay/petrol_price)
        petrol_tank=tank_size-petrol_filled 
        print(petrol_tank)
        average=(petrol_tank/distance)
        print(average)
        if average>10:
            print("This car is suitable")
        else:
            print("Please choose another car.")
    if user=="TIAGO":
        tank_size=30
        distance=int(input("How much kilometers you have to drive: "))
        pay=int(input("How much amount you're going to pay: "))
        petrol_filled=(pay/petrol_price)
        petrol_tank=tank_size-petrol_filled 
        print(petrol_tank)
        average=(petrol_tank/distance)
        print(average)
        if average>10:
            print("This car is suitable")
        else:
            print("Please choose another car.")
    if user=="FORTUNER":
        tank_size=40
        distance=int(input("How much kilometers you have to drive: "))
        pay=int(input("How much amount you're going to pay: "))
        petrol_filled=(pay/petrol_price)
        petrol_tank=tank_size-petrol_filled 
        print(petrol_tank)
        average=(petrol_tank/distance)
        print(average)
        if average>10:
            print("This car is suitable")
        else:
            print("Please choose another car.")
else:
    print(user,"This car is not avalaible")