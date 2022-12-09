from cardHolder import cardHolder
def print_menu(self):
        print("Please choose from one of the following:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
def deposit(cardHolder):
        try:
            deposit=float(input("How much money do you like to deposit: "))
            cardHolder.set_balance(cardHolder.get_balance()+deposit)
            print("Thank you for your money",str(cardHolder.get_balance()))
        except:
            print("Invalid Input")
def withdraw(cardHolder):
        try:
            withdraw=float(input("How much do you want to withdraw: "))
            if (cardHolder.get_balance() < withdraw):
                print("Not sufficent amount.")
            else:
                cardHolder.set_balance(cardHolder.get_balance()-withdraw)
                print("You can go ahead and withdraw")
        except:
            print("Invalid Input")
def check_balance(cardHolder):
        print("your current balance",cardHolder.get_balance())
if __name__=="__main__":
    current_user=cardHolder("","","","","")
#Creating a repo
    list_of_cardHolders=[]
    list_of_cardHolders.append(cardHolder("73456781",1234,"john","retre",123.45))
    list_of_cardHolders.append(cardHolder("73456731",1334,"kohn","qetre",123.35))
    list_of_cardHolders.append(cardHolder("7345341",1254,"dohn","detre",143.44))

    debitCardNum=""
    while True:
        try:
            debitCardNum=input("Please insert your debit card:")
            debitMatch=[holder for holder in list_of_cardHolders if holder.cardNum==debitCardNum]
            if(len(debitMatch)>0):
                current_user=debitMatch[0]
                break
            else:
                print("Card Number not recognized")
        except:
            print("Card Number not recognized")
    #Creating for pin
    while True:
        try:
            userPin=int(input("Please enter your PIN: ").strip())
            if (current_user.get_pin()==userPin):
                break
            else:
                print("Invalid PIN")
        except:
            print("Invaild PIN")
    print("Welcome",current_user.get_firstname())
    option=0
    while(option!=4):
        print_menu()
        try:
            option=int(input())
        except:
            print("INVALID INPUT PLEASE TRY AGAIN")
        if (option==1):
            deposit(current_user)
        elif(option==2):
            withdraw(current_user)
        elif(option==3):
            check_balance(current_user)
        elif(option==4):
            break
        else:
            option=0
    print("Thank you for visiting")
