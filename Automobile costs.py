#Corey Dew
#cs21
#excercise 4


def main():
    loan = float(input("Enter the monthly loan amount: "))
    insurance = float(input("Enter the monthly insurance amount: "))
    gas = float(input("Enter the monthly gas amount: "))
    oil = int(input("Enter the montly oil amount: "))
    tires = float(input("Enter the monthly tires amount: "))
    maintenance = int(input("Enter the monthly maintenance amount: "))
    month_expense = loan + insurance + gas + oil + tires + maintenance
    tot_month_expense(loan, insurance, gas, oil, tires, maintenance)
    tot_annual_expense(month_expense)
def tot_month_expense(loan, insurance, gas, oil, tires, maintenance):
    month_expense = loan + insurance + gas + oil + tires + maintenance
    print("Total monthly expense: $", month_expense)
def tot_annual_expense(month_expense):
    annual_expense = month_expense * 12
    print("Total annual expense: $", format(annual_expense, '.2f'))


main()

    
