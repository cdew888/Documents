#Corey Dew
#cs21

#Bmi = weight * 703 / height^2

x = float(input("Enter weight in pounds:"))
y = float(input("Enter height in inches:"))
bmi = x * 703 / y**2
if bmi < 18.5:
    print("to underweight")
else:
    bmi > 25
    print("to overweight")

print(bmi)
