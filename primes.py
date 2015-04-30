#Corey Dew
#cs21
#Question 17

def main():
    for num in range(1,101):
        result = is_prime(num)
        if result == True:
            print(num)
def is_prime(num):
    for x in range(2, num - 1):
        if num % x == 0:
            return False
        
    return True
main()
    
