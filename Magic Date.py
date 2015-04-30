#Ch.3 Problem 6 - Magic Date

#all input comes in numeric for e.g., 6/1/60
#ask user for month

#ask user for day

#ask for year

#perform our calculation: month*day

#compare month*day to year: month*day == year

#if equal, print "magic date"
#else if not equal, print "not magic date"

month = int(input("Enter a month numerically: "))
if month < 1 or month > 12:
    print("invalid month.")
else:
    day = int(input("Enter a date: "))

    if day < 1 or day > 31:
        print("Invalid day.")
    else:
        year = int(input("Enter the last two digits of a year: "))

        if year < 0 or year > 99:
            print("That date is magic!")
        else:

            if month * day == year:
               print("That date is magic!")

            else:
               print("That date is not magic.")
