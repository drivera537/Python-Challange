#import packages
import os
import csv

#Path collection for the Data
dataCSV = os.path.join('Resources','budget_data.csv')
dataFinal = os.path.join('Resources','budget_data.txt')

#Initialize variables
monthCount = 0
total = 0 
PreValue = 0 
profit = 0 
profitMax = 0 
profitMin = 0
plist = []

#Open and read CSV file
with open(dataCSV, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         profit =  iAmount - PreValue
         plist = plist + [profit]
         #Placeholder to track greatest increase in profits (financial analysis)
         if profitMax < profit:
            profitMax = profit
            profitMaxDate = month
         #Placeholder to track greatest decrease in profits (financial analysis)
         if profitMin > profit:
            profitMin = profit
            profitMinDate = month

         PreValue = iAmount   
         # Get total months (financial analysis)
         monthCount = monthCount + 1
         total += int(Amount)
         
average  = sum(int(i) for i in plist[1:87])/(monthCount-1)
average = round(average,2)

final = (
    f'Financial Analysis\n'
    f'----------------------------\n' 
    #total months
    f'Total Months : {monthCount}\n'
    #The total "Profit/Losses" 
    f'Total: $ {total}\n'
    #Average Change
    f'Average Change : {average}\n'
    # Greatest increase in profit
    f'Greatest Increase in Profits: {profitMaxDate} : ($ {profitMax})\n'
    # Greatest Decrease in profit
    f'Greatest Decrease in Profits: {profitMinDate} : ($ {profitMin})\n')
print(final)

with open(dataFinal, "w") as txtFile:
    txtFile.write(final)