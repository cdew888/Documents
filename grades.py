#Corey Dew
#cs21
#Question 3

def main():
    try:
        input_file = open('grades.dat', 'r')
        out_file = open('grades_out.dat', 'w')
        As = 0
        Bs = 0
        Cs = 0
        Ds = 0
        Fs = 0
        for line in input_file:
            int_grade = float(line)
            if int_grade < 60:
                out_file.write("F" + "\n")
                Fs += 1
            elif int_grade < 70:
                out_file.write("D" + "\n")
                Ds += 1
            elif int_grade < 80:
                out_file.write("C" + "\n")
                Cs += 1
            elif int_grade < 90:
                out_file.write("B" + "\n")
                Bs += 1
            else:
                out_file.write("A" + "\n")
                As += 1
        out_file.write('\n')
        input_file.close()
        numAs = As
        numBs = Bs
        numCs = Cs
        numDs = Ds
        numFs = Fs
        out_file.write('A:')
        for a in range(numAs):
            out_file.write('*')
        out_file.write("\n")   
        
        out_file.write('B:')
        for b in range(numBs):
            out_file.write('*')
        out_file.write("\n") 
        
        out_file.write('C:')
        for c in range(numCs):
            out_file.write('*')
        out_file.write("\n") 
        
        out_file.write('D:')
        for d in range(numDs):
            out_file.write('*')
        out_file.write("\n") 
        
        out_file.write('F:')
        for f in range(numFs):
            out_file.write('*')
        out_file.write("\n") 
        
        out_file.close()
    except IOError:
        print("ERROR: File does not exist")
    except ValueError:
        print("ERROR:Non-numeric data found in the file")
main()
    #try:
##        #grades_out.dat = open('grades.dat', 'a')

##        
##        print('A:', end='')
##        for i in range(numAs):
##            print('*', end='')
##        print()
##        grades_out.dat.close()
##    except IOError:
##        print("Error: IO Error has occured")
##    except ValueError:
##        print("Error:

main()
