#Corey Dew
#CS21
#question 4

speed = float(input("Enter speed of vehicle in mph: "))
hours = float(input("Enter hours traveled by vehicle: "))
while speed <= 0:
    print("invalid speed")
    speed = int(input("Enter speed of vehicle in mph: "))
while hours <= 0:
    print("invalid hours")
    hours = int(input("Enter hours traveled by vehicle: "))
else:
    t = 1
    while t <= hours:
        distance = speed * hours
        print(distance)
        t = t + 1
    
print("Hour\t Distance traveled\ n----------")

print(str(t)+ "\t" + str(format(speed * hours)))
