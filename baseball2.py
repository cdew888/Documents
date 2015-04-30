#Corey Dew
#cs21
#Baseball question

#Global constant for the base year
BASE_YEAR = 1903
SKIP_YEAR1 = 1904
SKIP_YEAR2 = 1994

def main():
    #Local dictionary variables
    year_dict = {}
    count_dict = {}

    #Open the file for reading
    input_file = open('WorldSeriesWinners.txt', 'r')

    #Read all the lines in the file into a list
    winners = input_file.readlines()

    #Fill the dictionaries with the team information.
    for i in range(len(winners)):
        team = winners[i].rstrip('\n')

        #Figure out in which year the team won
        #(take into account skipped years)

        year = BASE_YEAR + i
        #print(year,end=' ')
        if year >= SKIP_YEAR1:
            year += 1
        if year >= SKIP_YEAR2:
            year += 1
        #print(year)
        # Add information to year dictionary
        year_dict[str(year)] = team
        
        #Update counting dictionary
        if team in count_dict:
            count_dict[team] += 1
        else:
            count_dict[team] = 1
            
    #Recieve user input
    year = input("Enter a year in the range 1903-2009: ")
    
    #print results
    if year == '1904' or year == '1994':
        print("The world series wasn't played in the year", year)
    elif year < '1903' or year > '2009':
        print("The data for the year", year, "is not included in out database.")
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print("The team that won the world series in ", year, "is the ", winner, '.', sep='')
        print("They won the world series", wins, "times.")
        
#Call the main function.
main()
            
