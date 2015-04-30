#Corey Dew
#cs21
#Exercise 10

def main():
    tot_wins = 0
    try:
        in_file = open("WorldSeriesWinners.txt", 'r')
        winners_list = []
        for line in in_file:
            line = line.rstrip("\n")
            winners_list.append(line)
        in_file.close()
        find_team = input("What team are you looking for? ")
        for i in range(len(winners_list)):
            if winners_list[i] == find_team:
                tot_wins += 1
        print(find_team, "has won", tot_wins)
                
    except IOError:
        print("Error: File does not exist")
main()
