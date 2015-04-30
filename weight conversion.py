#ask user fo weight of package

#test if weight is <= 21lbs and weight >= 0
#if so, calculate shipping

#do same for 2-6 lb range

#6-10 range

#10+ range

#print shipping cost


weight = float(input("Enter the weight of a package: "))
if weight < 0:
    print("Invalid weight.")
elif weight >10:
    cost = weight * 4.75
elif weight >= 6:
    cost = weight * 4
elif weight >= 2:
    cost = weight * 3
else:
    cost = weight * 1.5
print("$" + str(cost) + " is the cost of shipping.") 
