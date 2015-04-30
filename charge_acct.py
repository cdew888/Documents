#Corey Dew
#cs21
#Excersie 5

def main():
    try:
        in_file = open("charge_accounts.txt", 'r')
        list_file = []
        for line in in_file:
            line = line.rstrip("\n")
            list_file.append(line)
        ch_acc = input("Enter a charge account number: ")
        if ch_acc in list_file:
                print(ch_acc, "was found in list and is valid")
        else:
            print(ch_acc, "was not found in list and is invalid")

        in_file.close() 
        print(list_file)

    except IOError:
        print("Error: File does not exist")
        

main()
