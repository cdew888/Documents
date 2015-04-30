#Corey Dew
#cs21
#Question 5

letters1 = ["A", "B", "C"]
letters2 = ["D", "E", "F"]
letters3 = ["G", "H", "I"]
letters4 = ["J", "K", "L"]
letters5 = ["M", "N", "O"]
letters6 = ["P", "Q", "R", "S"]
letters7 = ["T", "U", "V"]
letters8 = ["W", "X", "Y", "Z"]

user_num = input("Enter the telephone number in the format XXX-XXX-XXXX: ")

try:
    for ch in user_num:
        if ch in letters1:
            user_num = user_num.replace(ch, "2")
        
        elif ch in letters2:
            user_num = user_num.replace(ch, "3")
        
        elif ch in letters3:
            user_num = user_num.replace(ch, "4")
        
        elif ch in letters4:
            user_num = user_num.replace(ch, "5")
        
        elif ch in letters5:
            user_num = user_num.replace(ch, "6")
        
        elif ch in letters6:
            user_num = user_num.replace(ch, "7")
        
        elif ch in letters7:
            user_num = user_num.replace(ch, "8")
        
        elif ch in letters8:
            user_num = user_num.replace(ch, "9")
            
    print("The phone number is", user_num)
except:
    print("An error occurred")
