#Corey Dew
#cs21
#excercise 7


def main():
    A = int(input("Enter count of A seats: "))
    B = int(input("Enter count of B seats: "))
    C = int(input("Enter count of C seats: "))
    income_A(A)
    income_B(B)
    income_C(C)
    tot_income(A, B, C)
def income_A(A):
    income_a = A * 20
    print("Income from class A seats: $", income_a)
def income_B(B):
    income_b = B * 15
    print("Income from class B seats: $", income_b)
def income_C(C):
    income_c = C * 10
    print("Income from class C seats: $", income_c)
def tot_income(A, B, C):
    tot_inc = A * 20 + B * 15 + C * 10
    print("Total income: $", format(tot_inc, '.2f'))


main()
