#Corey Dew
#cs21
#Question 7

##uppercase = 0
##lowercase = 0
##digits = 0
##spaces = 0
##letters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
##letters2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
##letters3 = [""]

def main():
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0
    letters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letters2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters3 = [" ", "\n", "\t"]
    letters4 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    filename = input("Enter the file name: ")
    try:
        in_file = open(filename, 'r')
        for line in in_file:
            for ch in line:
                if ch in letters1:
                    uppercase = uppercase + 1
                
                
                elif ch in letters2:
                    lowercase = lowercase + 1
                

                elif ch in letters3:
                    spaces = spaces + 1
                
            
                elif ch in letters4:
                    digits = digits + 1
                
                       
        print("Uppercase letters:", uppercase)
        print("Lowercase letters:", lowercase)
        print("Digits:", digits)
        print("Spaces:", spaces)
        in_file.close()

    except IOError:
        print("ERROR: File does not exist")

main()
    
        
