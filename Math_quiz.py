#Corey Dew
#cs21
#chp.5 question 11

import random
# main function
def main():
    
    # Get numbers
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    
    # Display math problem
    display_problem(num1,num2)
    
    # Get user answer
    user_answer = get_answer()
    
    # Calculate correct answer
    correct_answer = num1 + num2
    
    # Display result
    show_result(correct_answer, user_answer)
    
#display the problem with first number on the first line and
# + and 2nd number of second line
def display_problem(num1,num2):
    print(format(num1, '5'))
    print("+", end="")
    print(format(num2, '4'))
    print('-----')
    
# The get_answer function gets and retyrns the user answer
def get_answer():
    input_answer = int(input("Enter sum of numbers: "))
    return input_answer

# The show_result function tells if user answer is correct or not
def show_result(correct_answer, answer):
    if correct_answer == answer:
        print("correct answer - Good Work!")
    else:
        print("incorrect... The correct answer is: ", correct_answer)

main()
