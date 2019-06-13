import os
import csv
import statistics

csvpath = os.path.join("budget_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     
    rowCounter = 0
    dateList = []
    priceList = []
    averagechange = []

    next(csvreader)
    first_row = next(csvreader)
    dateList.append(first_row[0])
    priceList.append(int(first_row[1]))

    previous_pl = first_row[1]

    for row in csvreader:
        dateList.append(row[0])
        priceList.append(int(row[1]))
        averagechange.append(int(row[1])-int(previous_pl))

        previous_pl = row[1]
            
    
    print ("Total Months: " + str(len(dateList)))
    print ("Total: " + "$" + str(sum(priceList)))
    print ("Average: " + str(statistics.mean(averagechange)))
    maximum_value = max(averagechange)
    minimum_value = min(averagechange)
    maximum_date = dateList[averagechange.index(maximum_value)+1]
    minimum_date = dateList[averagechange.index(minimum_value)+1]
    
    print (f"Date: {maximum_date} Value: {maximum_value}")    #"" can i add + (row[0]) and str to get the date? ""
    print (f"Date: {minimum_date} Value: {minimum_value}")
