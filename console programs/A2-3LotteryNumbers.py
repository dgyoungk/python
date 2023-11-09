#program that reads from the file pbnumbers.txt, puts them into a list
#then displays the 10 most common numbers and the 10 least common numbers
#based on frequency

#constants
FILENAME = "pbnumbers.txt"

def main():
    #gets list of all the winning numbers
    winningNums = getWinners()

    #gets dict of number counts in list winningNums
    freq = getCounts(winningNums)


    #gets list of top 10 values in freq
    top_ten = getTop10List(freq)

    finalTop10 = get10Dict(freq, top_ten)

    print("The 10 most common numbers:")
    print("----------------------------")

    for k, v in finalTop10.items():
        print(f"{k} appeared {v} times")


    print()
    
    #gets list of bottom 10 values in freq
    bot_ten = getBot10List(freq)

    finalBot10 = get10Dict(freq, bot_ten)

    print("The 10 least common numbers:")
    print("----------------------------")

    for k, v in finalBot10.items():
        print(f"{k} appeared {v} times")


##def get10Lowest(freq):
##    bottTen = {}
##    freqSorted = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
##
##    for count in range(10):
##        key, value = freqSorted.popitem()
##        bottTen[key] = value
##
##    return bottTen

def getTop10List(freq):
    counts = list(freq.values())
    finalists = [] * len(counts)
    top10 = [] * 10
    
    for index in counts:
        finalists.append(index)

    finalists.sort()
    finalists.reverse()

    for count in range(10):
        value = finalists[count]
        top10.append(value)
   
    return top10

def getBot10List(freq):
    counts = list(freq.values())
    finalists = [] * len(counts)
    bot10 = [] * 10

    for index in counts:
        finalists.append(index)

    finalists.sort()

    for count in range(10):
        value = finalists[count]
        bot10.append(value)

    return bot10

def get10Dict(freq, finalists):
    result = {}

    for k, v in freq.items():
        if v in finalists:
            result[k] = v

    return result
    

##def get10Highest(freq):
##    topTen = {}
##    freqSorted = dict(sorted(freq.items(), key=lambda x:x[1]))
##
##    for count in range(10):
##        key, value = freqSorted.popitem()
##        topTen[key] = value
##
##    return topTen        
    

def getCounts(numbers):
    freq = {}
    for item in numbers:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    return freq
    


def getWinners():
    winners = []
    try:
        inf = open(FILENAME, "r")

        line = inf.readline()

        while line != "":
            
            line = line.rstrip("\n")
            line = line.split(" ")

            for item in line:
                winners.append(item)

            line = inf.readline()
        

        inf.close()

        winners.sort()
            
    except:
        print("An error has occured")

    return winners

if __name__ == "__main__":
    main()
    
