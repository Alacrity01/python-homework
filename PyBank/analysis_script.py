import csv

budget_data = open('budget_data.csv')
type(budget_data)

csvreader = csv.reader(budget_data)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

months = []
month_max = ""
month_min = ""
delta_max = 0
delta_min = 0
net = 0
for r in rows:
    months.append(r[0])
    net += float(r[1])

    if int(r[1]) > int(delta_max):
        month_max = r[0]
        delta_max = int(r[1])

    elif int(r[1]) < int(delta_min):
        month_min = r[0]
        delta_min = int(r[1])

number_of_months = len(rows)
average = net / len(months)

budget_data.close()
report_data = (number_of_months,net,average,delta_max,delta_min)

# def report(number_of_months, net, average, delta_max, delta_min):
def report(report_data):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {number_of_months}")
    print(f"Total: {int(net)}")
    print(f"Average  Change: ${average:.2f}")
    print(f"Greatest Increase in Profits: {month_max} (${delta_max})")
    print(f"Greatest Decrease in Profits: {month_min} (${delta_min})")

report(report_data)
# report(number_of_months,net,average,delta_min,delta_max)
# Expected output:
#       Financial Analysis
#       ----------------------------
#       print(Total Months: 86
#       print(Total: $38382578
#       print(Average  Change: $-2315.12
#       print(Greatest Increase in Profits: Feb-2012 ($1926159)
#       print(Greatest Decrease in Profits: Sep-2013 ($-2196167)