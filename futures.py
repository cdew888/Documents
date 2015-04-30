#Corey Dew
#cs21
#Question 19

def main():
    account_value = int(input("Enter the present value of the account in dollars: "))
    monthly_interest = float(input("Enter the monthly interest rate as a percentage: "))
    while monthly_interest > 100:
        print("Invalid value")
        monthly_interest = float(input("Enter the monthly interest rate as a percentage: "))
    months = int(input("Enter the number of months: "))
    while months < 0:
        print("Invalid value")
        months = int(input("Enter the number of months: "))
    print("The information for your account is:")
    present_value = print("Present value: $", format(account_value, '.2f'))
    interest_rate = print("Interest Rate: %", format(monthly_interest, '.2f'))
    future_value(account_value, monthly_interest, months)
def future_value(account_value, monthly_interest, months):
    future_value = account_value * (1 + monthly_interest) ** months
    print("After", months, "months, the value of your account will be $ ", format(future_value, '.2f'))

    
main()
