# Import csv file
import os
import csv

# Set path for file
csvpath = r"C:\Users\Owner\Data_Analytics\Module_3_Python\python-challenge\PyBank\Resources\budget_data.csv"

# Lists to store data
months = 0
net_total = 0
changelist = []
avg_change = []
greatest_increase = []
greatest_decrease = []

print("Financial Analysis")
print(" ")
print("------------------------------")
print(" ")

# Find total of months
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        months = months + 1
    print("Total Months: "+str(months))
    print(" ")

# Find net total amount of "Profit/Losses" over the entire period
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        net_total = net_total + int(row[1])
    print("Total: " + "$" + str(net_total))
    print(" ")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    change = 0
    for row in csvreader:
        change += int(row[1])
        changelist.append(change)
    print("Average Change: " + "$" + str(sum(changelist)/(months-1)))
    print(" ")

#  The greatest increase in profits (date and amount) over the entire period
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        greatest_increase.append(float(row[1]))
differences = [greatest_increase[i+1] - greatest_increase[i] for i in range(len(greatest_increase)-1)]
max_difference = max(differences)
max_index = differences.index(max_difference)
max_date = None
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for i, row in enumerate(csvreader):
        if i == max_index + 1:
            max_date = row[0]
            break
print("Greatest Increase in Profits: " + str(max_date) +(" ") + ("($") + str(max_difference) + ")" )

# The greatest decrease in profits (date and amount) over the entire period
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data = list(csvreader)
greatest_decrease = float(data[0][1])
greatest_decrease_date = data[0][0]
for row in data:
    date = row[0]
    profit = float(row[1])
    if profit < greatest_decrease:
        greatest_decrease = profit
        greatest_decrease_date = date
print(" ")
print ("Greatest Decrease in Profit: " + str(greatest_decrease_date) + (" ") + ("($") + str(greatest_decrease) + ")" )

# Set variable for output file
folder_path = r"C:\Users\Owner\Data_Analytics\Module_3_Python\python-challenge\PyBank\Analysis"
output_file = "PyBank_Final.txt"
output_path = os.path.join(folder_path, output_file)

#  Open the output file
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis | ")
    output_file.write("Total Months: "+str(months) + " | ")
    output_file.write("Total: " + "$" + str(net_total) + " | ")
    output_file.write("Average Change: " + "$" + str(sum(changelist)/(months-1)) + " | ")
    output_file.write("Greatest Increase in Profits: " + str(max_date) +(" ") + ("($") + str(max_difference) + ")" + " | " )
    output_file.write("Greatest Decrease in Profit: " + str(greatest_decrease_date) + (" ") + ("($") + str(greatest_decrease) + ")" + " | " )