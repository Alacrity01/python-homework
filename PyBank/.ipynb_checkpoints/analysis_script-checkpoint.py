import csv

budget_data = open('budget_data.csv')
type(budget_data)

csvreader = csv.reader(budget_data)

header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
print(rows)

budget_data.close()



# create python script to calculate the following (by budget_data.csv)

months = 0 # total months included in the dataset
net = 0.0 #total amount of profit/losses over the entire period

average_change = net / months
greatest_increase = 0
greatest_decrease = 0


