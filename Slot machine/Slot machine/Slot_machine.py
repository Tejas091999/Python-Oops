
import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLUMNS = 3
symbol_count = {"A":2,"B":4,"C":6,"D":8}
symbol_value ={"A":5,"B":4,"C":3,"D":2}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol]*bet
                winnings_lines.append(line+1)
    return winnings_lines,winnings
def get_slot_machine_run(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()
def deposit():
    while True:
        amount=int(input("What amount would you like to deposit: "))
        if amount >= 0:
            break
        else:
            print("Amount must be greater than 0")
    return amount
def get_num_of_lines():
    while True:
        lines = int(input("How many lines do you want to bet: "))
        if 1<=lines<MAX_LINES:
            break
        else:
            print("Please enter a valid number of lines!")
    return lines
def get_bet():
    while True:
        amount=int(input("What would you like to bet: "))
        if MIN_BET<=amount<=MAX_BET:
            break
        else:
            print(f"Amount must be between {MIN_BET} and {MAX_BET} ")
    return amount
def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print("You do not have enough amount to bet!")
        else:
            break
    print(f"You're betting {bet} on {lines} lines .The total bet is {total_bet}")
    slots = get_slot_machine_run(ROWS,COLUMNS,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won {winnings}!!")
    print(f"You're winnings lines {winnings_lines}. ")
main()


