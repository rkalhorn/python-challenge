import csv

cvsPath = 'Resources/election_data.csv'

# Function that will print given string to both given output file and to the screen
def printme(str,wr):
   wr.writerow([str])
   print(str)
   return

votes=[]
candidates=[]
candidateVoteCount=[]

# Search through budget data to find election results
with open(cvsPath, newline='') as csvfile:
    # Skips headerline
    csvfile.readline()
    # CSV reader specifies delimiter and variable that holds contents
    electionData = csv.reader(csvfile, delimiter=",")
  
    # The total number of votes cast
    for row in electionData:
        votes.append(row[2])
    numVotes = len(votes)
    
# Create candidate list
candidates=list(set(votes))

# Find the number of votes for each candidate
for candidate in candidates:
    candidateVoteCount.append(votes.count(candidate))
    

# Write output to file and screen. 
# Seems that this could be done using logging, but in class we discussed writer. 
# So I will use writer with the function printme that I wrote above.
# Set variable for output file
outPath = ("output_file.csv")

# Open the output file
with open(outPath, "w", newline="") as datafile:
    # By including delimiter="\t" this eliminates quotes that were showing up around lines with formatted numbers.
    writer = csv.writer(datafile,delimiter="\t")

    # Print output
    printme("Election Results",writer)
    printme("-------------------------------",writer)
    printme((str("Total Votes: ")+ '{:,.0f}'.format(numVotes)).strip('"\''),writer)
    #printme(str("Total Votes: ")+ str(numVotes),writer)
    printme("-------------------------------",writer)
    for candidate in candidates:
        candidateVoteCount.append(votes.count(candidate))
        mystr='{:,.1f}%'.format(int(candidateVoteCount[-1])/numVotes*100)
        printme(str(candidate)+ ": "+mystr+ " ("+'{:,.0f}'.format(candidateVoteCount[-1])+")",writer)
    printme("-------------------------------",writer)
    printme("Winner: "+str(candidates[candidateVoteCount.index(max(candidateVoteCount))]),writer)
    printme("-------------------------------",writer)
   