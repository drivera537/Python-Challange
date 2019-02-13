import csv
import os

dataFile = os.path.join('Resources','election_data.csv')
dataFinal = os.path.join('Resources','election_data.txt')

# Need a list for names, votes per candidate, percentage & totalVotes
runners = []
numOfVotes = []
perVotes = []
total = 0

with open(dataFile, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total += 1 

        #add new candidate to the list with a vote,
        #if already ammend a vote to it
        if row[2] not in runners:
            runners.append(row[2])
            index = runners.index(row[2])
            numOfVotes.append(1)
        else:
            index = runners.index(row[2])
            numOfVotes[index] += 1

    # percentage list
    for votes in numOfVotes:
        percentage = (votes/total) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        perVotes.append(percentage)
    
    # winning candidate
    poolWinner = max(numOfVotes)
    index = numOfVotes.index(poolWinner)
    winner = runners[index]

#overall Results
for i in range(len(runners)):

#result
    conclusion = (
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {str(total)}\n"
    f"--------------------------\n"
    f"{runners[0]}: {str(perVotes[0])} ({str(numOfVotes[0])})\n"
    f"{runners[1]}: {str(perVotes[1])} ({str(numOfVotes[1])})\n"
    f"{runners[2]}: {str(perVotes[2])} ({str(numOfVotes[2])})\n"
    f"{runners[i]}: {str(perVotes[i])} ({str(numOfVotes[i])})\n"
    f"--------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------")
print(conclusion)

with open(dataFinal, "w") as txtFile:
    txtFile.write(conclusion)