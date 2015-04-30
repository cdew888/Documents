#Corey Dew
#cs21
#question 3

total = 0
x = float(input("Enter amount budgeted for the month:"))
y = float(input("Enter an amount spent(0 to quit): "))
while y != 0:
    total += y
    y = float(input("Enter and amount spent(0 to quit): "))
    
if total >= x:
    print("you are" ,total - y, "over budget. Not good")
else:
    print("you are" ,total + y, "under budget. Good job")
    print("Budgeted:" ,x,)
