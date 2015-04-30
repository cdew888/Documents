#Corey Dew
#cs21
#chp.5 question 15

def main():
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))
    average = calc_average(score1, score2, score3, score4, score5)
    print("score\t\tnumeric grade\tletter grade")
    print("-------------------------------------------")
    print("score 1:\t\t", score1, "\t\t", determine_grade(score1))
    print("score 2:\t\t", score2, "\t\t", determine_grade(score2))
    print("score 3:\t\t", score3, "\t\t", determine_grade(score3))
    print("score 4:\t\t", score4, "\t\t", determine_grade(score4))
    print("score 5:\t\t", score5, "\t\t", determine_grade(score5))
    print("------------------------------------------------------")
    print("Average score:\t", average, "\t\t", determine_grade(average))
def calc_average(s1, s2, s3, s4, s5):
    return (s1 + s2 + s3 +s4 + s5) / 5.0
def determine_grade(score):
          if score >= 90:
              return "A"
          elif score >= 80:
              return "B"
          elif score >= 70:
              return "C"
          elif score >= 60:
              return "D"
          else:
              return "F"

main()
          
