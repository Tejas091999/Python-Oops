print("Turf accounting.")
rate_60=1000
rate_90=1500 
rate_120=1800
owner=int(input("How many minutes do you want to play: "))
if owner==60:
    no_players=int(input("How many players are playing: "))
    payment=(rate_60/no_players)
    print("Amount per person",payment)
    online=int(input("How many of them are online payment: "))
    online_pay=online*payment
    print(online_pay)
    cash=int(input("How many them are paying cash: "))
    cash_pay=cash*payment
    print(cash_pay)
    total_pay=(online_pay)+(cash_pay)
    print(total_pay)
    if total_pay==rate_60:
        print("You've collected all money")
    elif total_pay>rate_60:
        print("Someone payed extraaa")
    else:
        print("There is still someone left to pay..")
elif owner==90:
    no_players=int(input("How many players are playing: "))
    payment=(rate_90/no_players)
    print("Amount per person",payment)
    online=int(input("How many of them are online payment: "))
    online_pay=online*payment
    print(online_pay)
    cash=int(input("How many them are paying cash: "))
    cash_pay=cash*payment
    print(cash_pay)
    total_pay=(online_pay)+(cash_pay)
    print(total_pay)
    if total_pay==rate_90:
        print("You've collected all money")
    elif total_pay>rate_90:
        print("Someone payed extraa")
    else:
        print("There is still someone left to pay..")
elif owner==120:
    no_players=int(input("How many players are playing: "))
    payment=(rate_120/no_players)
    print("Amount per person",payment)
    online=int(input("How many of them are online payment: "))
    online_pay=online*payment
    print(online_pay)
    cash=int(input("How many them are paying cash: "))
    cash_pay=cash*payment
    print(cash_pay)
    total_pay=(online_pay)+(cash_pay)
    print(total_pay)
    if total_pay==rate_120:
        print("You've collected all money")
    elif total_pay>rate_120:
        print("Someone payed extraa")
    else:
        print("There is still someone left to pay..")