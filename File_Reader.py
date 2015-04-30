#Corey Dew
#cs21
#chapter 6 question 7

#import random

#main():
    
    #prompt user for file name

    #prompt user for number of random numbers to write to the file

    #write those numbers to the file:
        #open the file('w')
        #loop over

import random

def main():
    filename = input("Enter the file name to which results should be wrtten: ")
    num_randoms = int(input("Enter number of random numbers to write: "))

    outFile = open(filename, 'w')

    for i in range(num_randoms):
        randNum = random.randint(1,500)
        outFile.write(str(random) + '\n')

    outFile.close()

main()
