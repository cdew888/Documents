#Super Electric ATM Machine
#cs21

pin = 8008
pin_attempts = 0
checkings_acc = 500
savings_acc = 500

pin_attempts = int(input("Enter four digit pin:"))
while pin_attempts != 8008:
    print("invalid pin")
    pin_attempts = int(input("Enter four digit pin: "))
if pin == 8008:
    options = int(input("Press 1 for Checkings Account or press 2 for Savings Account: "))
    if options == 1:
        print("You have $", checkings_acc, "in your Checkings Account")
    elif options == 2:
        print("You have $", savings_acc, "in your Savings Account")


