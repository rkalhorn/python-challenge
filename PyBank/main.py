import csv

cvsPath = 'Resources/budget_data.csv'

# Function that will print given string to both given output file and to the screen
def printme(str,wr):
   wr.writerow([str])
   print(str)
   return

months = []
rev = []
greatestInc=[0,0]
greatestDec=[0,0]
totalRev = 0


#search through budget data
with open(cvsPath, newline='') as csvfile:
  # skips headerline
  csvfile.readline()
  # CSV reader specifies delimiter and variable that holds contents
  budget = csv.reader(csvfile, delimiter=",")
  
  # Create month and revenue lists
  for row in budget:
    months.append(row[0])
    rev.append(int(row[1]))
    #check to see if we are at least on line 2
    if(len(rev)>1):
      #set current monthly change to this line's rev - last line's rev
      curChange = rev[-1]-rev[-2]
      
      #check to see if current change is greater than previous greatest increase.
      #If so change the month (stored in index 0) and change (stored in index 1) of greatstInc
      if(greatestInc[1]<curChange):
        greatestInc[1]=curChange
        greatestInc[0]=months[-1]
      #check to see if current change is less than previous greatest decrease.
      #If so change the month (stored in index 0) and change (stored in index 1) of greatstDec
      elif(greatestDec[1]>curChange):
        greatestDec[1]=curChange
        greatestDec[0]=months[-1] #Since we are stating this as the greatest decrease it should be positive. A negative decrease would actually be an increase.

  averageChangeProfitLoss = (int(rev[-1])-int(rev[0]))/(len(rev)-1)

# Seems that this could be done using logging, but in class we discussed writer. 
# So I will use writer with the function printme that I wrote above.
# Set variable for output file
outPath = ("output_file.csv")

# Open the output file
with open(outPath, "w", newline="") as datafile:
    # By including delimiter="\t" this eliminates quotes that were showing up around lines with formatted numbers.
  writer = csv.writer(datafile,delimiter="\t")

  printme("Total Months: "+str(len(set(months))),writer)
  printme("Total Revenue: "+'${:,.0f}'.format(sum(int(i) for i in rev)),writer)
  printme("Average Monthly Revenue Chanage " + '${:,.0f}'.format(averageChangeProfitLoss),writer)
  printme("Greatest Monthly Revenue Increase "+str(greatestInc[0])+ " ("+'${:,.0f}'.format(greatestInc[1]) +")",writer)
  printme("Greatest Monthly Revenue Decrease "+str(greatestDec[0])+ " ("+'${:,.0f}'.format(greatestDec[1])+")",writer)
            
