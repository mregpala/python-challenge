#Created By Michael Regpala
#Created on 2021-01-02
#Purpose Homework assignment to track revenue

#Modified

import os
import csv

#Declare infile and outfile path
budgetcsv = os.path.join(".","Resources","budget_data.csv")
summarytxt = os.path.join(".","analysis","budget_summary.txt")

totalmonths = 0
totalprofitloss = 0 
priormonthprofitloss = 0
totalprofitchange = 0

#Decoare list. plschange will be a list of tuples.  
plchange = []

with open(budgetcsv) as infile:
    csvreader = csv.reader(infile)
    header = next(csvreader,None)
    for row in csvreader:
      currentprofitloss = float(row[header.index('Profit/Losses')])
      month = row[header.index('Date')]
      if totalmonths == 0:
          #First month will not have a change
          priorprofitloss = currentprofitloss
      else:
          profitlosschange = currentprofitloss - priorprofitloss
          plchange.append((profitlosschange,month))
          totalprofitchange = totalprofitchange + profitlosschange
          priorprofitloss = currentprofitloss
      totalmonths = totalmonths + 1
      totalprofitloss = totalprofitloss + float(row[header.index('Profit/Losses')])


plchange.sort(reverse=True)
averagechange = totalprofitchange / (totalmonths - 1)
#Print to terminal
print(f'Total Months: {totalmonths}')
print('Total Profit: $%1.0f' %totalprofitloss)
print('Average Change: $%.2f' %averagechange )
print(f'Greatest Increase in Profits: {plchange[0][1]} (${int(plchange[0][0])})')
print(f'Greatest Decrease in Profits: {plchange[-1][1]} (${int(plchange[-1][0])})')

#Print to file
with open(summarytxt,"w") as outfile:
    outfile.write(f'Total Months: {totalmonths}\n')
    outfile.write('Total Profit: $%1.0f\n' %totalprofitloss)
    outfile.write('Average Change: $%.2f\n' %averagechange )
    outfile.write(f'Greatest Increase in Profits: {plchange[0][1]} (${int(plchange[0][0])})\n')
    outfile.write(f'Greatest Decrease in Profits: {plchange[-1][1]} (${int(plchange[-1][0])})\n')



    