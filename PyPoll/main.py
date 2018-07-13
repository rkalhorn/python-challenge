import csv

cvsPath = 'Resources/election_data.csv'

votes=[]
candidates=[]
candidateVoteCount=[]

#search through budget data to find election results
print("Election Results")
print("-------------------------------")
with open(cvsPath, newline='') as csvfile:
    # skips headerline
    csvfile.readline()
    # CSV reader specifies delimiter and variable that holds contents
    electionData = csv.reader(csvfile, delimiter=",")
  
     # Create candidate list
    for row in electionData:
        votes.append(row[2])
    numVotes = len(votes)
    #The total number of votes cast
    print("Total Votes: "+ '{:,.0f}'.format(numVotes))
    print("-------------------------------")

    candidates=list(set(votes))
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    for candidate in candidates:
        candidateVoteCount.append(votes.count(candidate))
        print(str(candidate)+ ": "+'{:,.1f}%'.format(int(candidateVoteCount[-1])/numVotes*100)+ " ("+'{:,.0f}'.format(candidateVoteCount[-1])+")")

#The winner of the election based on popular vote.
    print("-------------------------------")
    print("Winner: "+str(candidates[candidateVoteCount.index(max(candidateVoteCount))]))
    print("-------------------------------")

