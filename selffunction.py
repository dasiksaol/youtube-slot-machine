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
        

