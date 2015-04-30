#Corey Dew
#cs21
#Exercise 7

def main():
    tot_score = 0
    tot_correct = 0
    tot_wrong = 0
    wrong_list = []
    try:
        answer_sheet = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
        student_answers = open("student_solution.txt", 'r')
        student_answer_list = []
        wrong_list = []
        for line in student_answers:
            line = line.rstrip("\n")
            student_answer_list.append(line)
        print("Your answer sheet: ", student_answer_list)
    

        for i in range(len(answer_sheet)):
            if answer_sheet[i] == student_answer_list[i]:
                tot_correct += 1
            else:
                tot_wrong += 1
                wrong_list.append(i + 1)
        if tot_correct >= 15:
            print("You have passed the test.")
        else:
            print("You have failed the test.")
        print("You have", tot_correct, "questions correct")
        print("You have", tot_wrong, "questions correct")
        print("These are the questions you have wrong: ", wrong_list)
    except:
        print()
##                    
##            
##        for line in student_answers:
##            line = student_answers.rstrip("\n")
##            student_answers.append(line)
##        
##        while tot_score < len(answer_sheet):
##                if answer_sheet[tot_score] == student_answers:
##                    tot_correct += 1
##                    tot_score += 1
##                else:
##                    tot_wrong += 1
##                    wrong_list.append(tot_score)
##                    tot_score += 1
##                    
##            if tot_score >= 15:
##                print("You have passed the test")
##                print("You have", tot_correct, "correct answers")
##                print("You have", tot_wrong, "wrong answers")
##            else:
##                print("You have failed the test")
##                print("You have", tot_correct, "correct answers")
##                print("You have", tot_wrong, "wrong answers")
##
##                student_answers.close()
##    except IOError:
##        print("Error: File does not exist")
##
main()
