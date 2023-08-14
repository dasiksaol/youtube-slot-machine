from selffunction import *
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

symbol_value={
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1
}

balance = deposit()
line = get_line()
bet = get_bet()
slot = get_slot_machine(ROWS, COLS, symbol_count)
print_slot_machine(slot)
print(balance, line, bet)