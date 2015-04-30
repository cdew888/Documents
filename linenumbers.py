#Corey Dew
#cs21
#Question 1

def main():
    try:
        num = 0
        file_name = input("Enter the file name: ")
        user_file = open(file_name, 'r')
        out_file = open("ln" + file_name, 'w')
        for line in user_file:
            num += 1
            line = str(num) + ":" + (line)
            out_file.write(line)
    except:
        print("An error occurred.")
        user_file.close()
        out_file.close()
        
main()
    
