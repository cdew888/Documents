#Corey Dew
#cs21
#Question 14

def main():
    try:
        m = int(input("Enter objects mass in kilograms: "))
        v = int(input("Enter objects velocity in meters per second: "))
        k_e = kinetic_energy(m, v)
        print("The object has", k_e, "amounts of kinetic energy")
    except ValueError:
        print("ERROR: Mass and Velocity must be valid numbers")
def kinetic_energy(m, v):
    k_energy = 0.5 * m * v ** 2
    return k_energy

main()
