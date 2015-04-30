#Corey Dew
#cs21

# n! = n * n - 1 * n - 2 * ... 1
# 5! = 5 * 4 * 3 * 2 * 1

fact = 1
n = int(input("What number would you like to factorialize? "))
for num in range(1, n + 1):
    fact = fact * num
    print(fact)

##    #or
##def main():
##    n = int(input("What number would you like to factorialize? "))
##    factorialize(n)
##def factorialize(N):
##    fact = 1
##    for num in range(1, N + 1):
##        return fact
##main()

