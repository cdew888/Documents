#Corey Dew
#cs21

#60 seconds = 1 minute
#3,600 seconds = 1 hour
#86,400 seconds = 1 day


seconds = float(input("Enter number of seconds:"))

days = seconds // 86400
remainder_seconds = seconds % 86400
print(days)

hours = seconds // 3600
remainder_seconds % 3600
print(hours)

minutes = seconds // 60
print(seconds)

