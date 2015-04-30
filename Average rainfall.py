#Corey Dew
#cs21
#question 5

total = 0
n = int(input("Enter number of years: "))

for x in range(1, n + 1):
    print("for year" ,x,)

    for months in range(1,13):
        rainfall = float(input("Enter rainfall amount for month in inches: "))
        total += rainfall
print(total)
print("average rainfall: ",total / (12 * n))
