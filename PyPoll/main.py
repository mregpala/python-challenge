#Created By Michael Regpala
#Created on 2021-01-03
#Purpose Homework assignment to summarize election results

#Modified
import os
import csv

#Declare infile and outfile path
csvfile = os.path.join(".","Resources","election_data.csv")
summarytxt = os.path.join(".","analysis","election_summary.txt")

#Initialize dictionary
electdict = dict()

totalvotes = 0

with open(csvfile) as infile:
    csvreader = csv.reader(infile)
    header = next(csvreader,None)
    for row in csvreader:
        candidate = row[header.index('Candidate')]
        if len(electdict) == 0:
            #electdict[row[header.index('Candidate')]]
            electdict[candidate] = 1
        else:
            if candidate not in electdict:
                electdict[candidate] = 1
            else:
                electdict[candidate] = electdict[candidate] + 1
        totalvotes = totalvotes + 1

sorteddict = sorted(electdict.items(), key=lambda x: x[1], reverse=True)
print("Election Results") 
print("-------------------------")  
print(f"Total Votes {totalvotes}") 
print("-------------------------") 
for i in sorteddict:
    pctvotes = round((i[1]/totalvotes) * 100,3)
    print(f'{i[0]}: {pctvotes}% ({i[1]})')             
print("-------------------------") 
print(f'Winner: {sorteddict[0][0]}')
print("-------------------------")  

with open(summarytxt,"w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes {totalvotes}\n")
    outfile.write("-------------------------\n") 
    for i in sorteddict:
        pctvotes = round((i[1]/totalvotes) * 100,3)
        outfile.write(f'{i[0]}: {pctvotes}% ({i[1]})\n') 
    outfile.write("-------------------------\n")    
    outfile.write(f'Winner: {sorteddict[0][0]}\n')
    outfile.write("-------------------------")    
