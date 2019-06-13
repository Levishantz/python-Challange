import os 
import csv
import statistics
import collections


csvpath = os.path.join("election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 

    rowCounter = 0
    votes = []
    candidates = []


    for row in csvreader:
        if(rowCounter > 0):

            votes.append(row[0])
            candidates.append(row[2])

        rowCounter+=1

votecount = (collections.Counter(candidates))
# print(votecount)

for name, votes in votecount.items():
    print(f"Name: {name} Votes: #{votes} %{(int(votes)/sum(votecount.values()))*100:.2f}")
