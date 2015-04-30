#Corey Dew
#cs21
#exercise 8


def main():
    wall_space = int(input("Enter wall space in square feet: "))
    paint_price = int(input("Enter paint price per gallon: "))
    paint_gallon = int(input("Gallons of paint: "))
    labor_hours = paint_gallon * 8
    paint_charges = paint_price * paint_gallon
    print("Paint charges: $", format(paint_charges, '.2f'))
    labor_charges = paint_gallon * labor_hours
    print("Labor charges: $", format(labor126_charges, '.2f'))
    total_cost = paint_charges + labor_charges
    print("Total cost: $", format(total_cost, '.2f'))

main()
    
