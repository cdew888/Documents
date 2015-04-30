#Corey Dew
#cs21
#question 6 File analysis

codes = {}
code1 = open('codes.txt', 'r')
for line in code1:
    ch1 = line[0]
    ch2 = line[2]
    codes[ch1] = ch2
    
unique = []
unique2 = []
both = []
first_but = []
second_but = []
either = []
try:
    file_name = input("Enter a file: ")
    file2_name = input("Enter another file: ")
    in_file = open(file_name, 'r')
    in2_file = open(file2_name, 'r')

    words = in_file.read()
    words2 = in2_file.read()
    wordlist = words.split()
    wordlist2 = words2.split()

    set1 = set(unique)
    for word in wordlist:
        set1.add(word)
    set2 = set(unique2)
    for wordz in wordlist2:
        set2.add(wordz)
        
    print("List of unique words in", file_name, "as a list", set1)
    print("List of unique words in", file2_name, "as a list", set2)
    print("List of words in both files", set1.intersection(set2))
    print("List of words in", file_name, "but not in", file2_name, "as a list", set1.difference(set2))
    print("List of words in", file2_name, "but not it", file_name, "as a list", set2.difference(set1))
    print("List of words in either", file_name, "or", file2_name, "as a list", set1 | set2)
    in_file.close()
    in2_file.close()
    
except IOError:
    print("Error: file does not exist")
except:
    print("An error has occurred")
