#Corey Dew
#cs21
#Question 10

alphabet1 = "abcdefghijklmnopqrstuvwxyz"
counts = [0]*26
index = 0
max_total = 0
user_input = input("Enter a string: ")
user_input = user_input.lower()

try:
    print("The most frequently occurring letter(s):")
    for ch in user_input:
        
        if ch in alphabet1:
            index = alphabet1.find(ch)
            
            counts[index]=counts[index] + 1
    max_num = (max(counts))
    for i in range(len(counts)):
        if counts[i] == max_num:
            print(alphabet1[i], end='')
            
except:
    print("An error has occurred")
