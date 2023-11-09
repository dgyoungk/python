#program that reads from the file WorldSeriesWinners.txt, lets users enter
#a team name and see how many wins that team has


#constants
FILENAME = "WorldSeriesWinners.txt"

def main():
    #gets the list of teams that are in the file FILENAME
    teams = getTeams()        

    print("World Series Winners:")

    count = 0

    winner = input("Enter a team name to see how many times the team has won: ")

    for win in teams:
        if winner == win:
            count += 1

    print(f"The {winner} have won {count} times")


def getTeams():
    try:
        winners = list()

        years = list(range(1902, 2019))

        year = 1
            
        inf = open(FILENAME, "r")

        champ = inf.readline()

        while champ != "" and year < len(years):
            winners.append(champ.rstrip("\n"))
            champ = inf.readline()
            year += 1

        inf.close()
            
    except IOError:
        print("No such file exists")
        return champs
    except IndexError:
        print("The index is out of range. Fix it")
        exit()


    return winners
        

if __name__ == "__main__":
    main()
            
    
