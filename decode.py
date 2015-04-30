#Corey Dew
#cs21
#decode question


codes = {}
code1 = open('codes.txt', 'r')
for line in code1:
    ch1 = line[0]
    ch2 = line[2]
    codes[ch1] = ch2
    
print("Welcome to my encryption program")
print("You can choose to encrypt a file or decrypt and encrypted file")
option = input("Would you like to (1) Encrypt a file, (2) Decrypt a file? ")
try:
    if option == '1':
        file_name = input("Enter name of input file: ")
        out_file = input("Enter name of the output file: ")
        in_file = open(file_name, 'r')
        output_file = open(out_file, 'w')
        for line in in_file:
            for ch in line:
                if ch in codes:
                    output_file.write(codes[ch])
                    
                else:
                    output_file.write(ch)
                    
        print("Writing encrypted data to", out_file)
        in_file.close()
        output_file.close()
        code1.close()
        
    elif option == '2':
        file_name = input("Enter name of input file: ")
        out_file = input("Enter name of the output file: ")
        in_file = open(file_name, 'r')
        output_file = open(out_file, 'w')
        for line in in_file:
            for ch in line:
                if ch in codes:
                    output_file.write(codes[ch])
                else:
                    output_file.write(ch)
        print("Writing decrypted data to", out_file)
        in_file.close
        output_file.close
        code1.close()


except IOError:
    print('Error: File was not found')
except KeyError:
    print('Error: Key does not exist')
                    
                
    
