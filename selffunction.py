import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count={
    "A": 4,
    "B": 6,
    "C": 8,
    "D": 10
}

def deposit():
    while True:
        balance = input("How much do you want to deposit? $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("Please Enter an amount greater than 0")
        else:
            print("Please Enter a Number")
    return balance
        
def get_line():
    while True:
        line = input(f"How many line do you want to bet on?(1-{MAX_LINE}) :")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print(f"Please Enter a valid amount (1-{MAX_LINE})")
        else:
            print("Please Enter a Number")
    return line

def get_bet():
    while True:
        amount = input("How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a valid amount ({MIN_BET}-{MAX_BET})")
        else:
            print("Please Enter a Number")
    return amount

def get_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()
        


