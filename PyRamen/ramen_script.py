# import csv
# import csv
from pathlib import Path

# from tkinter import N
# import menu_data.csv as menu
# import sales_data.csv as sales

# budget_data = open('budget_data.csv')
# type(budget_data)
# csvreader = csv.reader(budget_data)

# menu items one to many <- unique identifier
# one for one relationship in the menu items-> one name for each item
# many to one for sales data items->

# menu items will be called as a foreign key relationship


# zipping
#     L1 = ["X", "Y", "Z"]
#     L2 = [5,6,8]
#     dict1 = dict( zip(L1,L2) )
#     print(dict1)

menu_path = Path("Resources/menu_data.csv")
open_menu = open(menu_path, 'r')
for line in open_menu:
	header = line.strip()
	break
menu_keys = header.split(",")
next(open_menu)
menu = []

with open_menu as file:
	for line in file:		
		row = line.strip()
		row = line.strip().split(',')
		item_details = [row[0], row[1],row[-2],row[-1]]

		menu.append(item_details)

sales_path = Path("Resources/sales_data.csv")
open_sales = open(sales_path, 'r')
for line in open_sales:
	header = line.strip()
	break
sales_keys = header.split(",")
next(open_sales)
sales = []  #INSTRUCTIONS SPECIFIED**********************

with open_sales as file:
	for line in file:		
		row = line.strip().split(",")
		sales.append([row[-1],row[-2]]) # [sales_item,quantity]

report = {}

# initialize the report dictionary
for sales_row in sales:
	sales_item = sales_row[0]
	if sales_item in report:
		continue
	else:
		report[sales_item] = {
		"01-count": 0,
		"02-revenue": 0,
		"03-cogs": 0,
		"04-profit": 0,
    	}

# check for sales of each menu item and add
for menu_row in menu:
	item = menu_row[0]
	
	for sales_row in sales:
		sales_item = sales_row[0]	
		if item == sales_item:
			price = float(menu_row[-2])
			cost = float(menu_row[-1])
			quantity = int(sales_row[1])
			profit = price - cost

			report[sales_item]["01-count"] += quantity
			report[sales_item]["02-revenue"] += price * quantity
			report[sales_item]["03-cogs"] += cost * quantity
			report[sales_item]["04-profit"] += profit * quantity

			# print(report)
			# break
	else:
		# print(f"{sales_item} does not equal {item}! NO MATCH!")
		continue

open_report = open("report.txt","w")
report_text = ""
for a in report:
	# open_report.write(str(report))
	# print(f"{a} {report[a]}")
	report_text += str(f"{a} {report[a]}\n")

print(report_text)

open_report.close()
'''
reference of menu:
['item', 'category', 'price', 'cost']
'''
# print(report)



	# for i in row:

# 	print(row)
# 	count+=1 
# 	print(count)
	# for i in range(len(menu_keys)):
	# for i in range(2):#len(menu_keys)):#testing
	# 	item = menu[i][0]
	# 	if item in report.keys():
	# 		# print("TRUE")
	# 		quantity = sales[i][-2]
	# 		price = menu[-2]
	# 		cost = menu[-1]
	# 		profit = price - cost
	# 		report[item]["01-count"] += quantity
	# 		report[item]["02-revenue"] += price * quantity
	# 		report[item]["03-cogs"] += cost * quantity
	# 		report[item]["04-profit"] += profit * quantity
	# 	else: 
			# print("not found")
			# print(f"NO MATCH FOUND! {item} not found in sales_data")
			# print("{sales_item} does not equal {item}! NO MATCH!")
	# 		break
	# 	break
	# break
# print(report.keys())
# print(report)
# print(errors)
# print(report[item]["01-count"])
# test_row = 'house salad,appetizers,"mixed greens, cherry tomatoes, cucumber, house ginger dressing",4,2'
# split_test = test_row.split('"')
# split_test = test_row.split(',')
# print(split_test)
# print(menu_keys)
# print(split_test[0])
# print(split_test[1])

# print("omit [2]!")
# print(menu[0])
# print(type(menu[0]))
# print(report["miso crab ramen"])
# menu_dict = {}
# menu_dict = dict( zip(menu_keys,menu_items) )
# print(menu_dict)

# '''
# count = 0
# with open(menu_path, 'r') as file:
# 	count += 1
# 	text = file.read()
# 	menu.append(text)
# '''

# print(sales_keys)

# print(sales[0][-2])
# print(sales[1][-2])

# print(sales_keys[-2])


	# text = file.read()
	# menu.append(text)
	# text = file.read()
	# menu.append(text)
	
# print(menu[-1])

# sales_path = Path("Resources/sales_data.csv")

# with open(sales_path, 'r') as file:
# 	text = file.read()
# 	print(text)



# output_path = Path("output.txt")

# with open(output_path,'w') as file:
# 	file.write(text)




# p = Path('.')
# [x for x in p.iterdir() if x.is_dir()]

# list(p.glob('**/*.py'))

# q = p / 'Resources' / 'sales_data.csv'
# q
# q.resolve()

# q.exists()

# q.is_dir()

# with q.open() as f: print(f.readline())
# with q.open() as f: print(f.readline())
# with q.open() as f: print(f.readline())

# r = Path('./Resources')

# print(r)
# r = Path('./PyRamen//Resources')
# print(type(r))
# print(r)
# menu = r.open('menu_data.csv',r)

# f = open("menu_data.csv", "r")
# print(f.read())


# with f.open('menu_data.csv') as csv: csv.reader()





# f = open("D:\\myfiles\welcome.txt", "r")

# print(f.read())
# print(menu)
# with r.open() as csv: csv.reader()


# q = list(p.iterdir())
# print(q[1])
# print(type(q[1]))

# with q.open() as f: csvreader.readline()
# print(f)

# x_list = [x for x in p.iterdir() if x.is_dir()]
# print(f"x list is: {x_list})

# p = Path('/etc')
# q = p / 'init.d' / 'reboot'
# q
# print(q)
# q.resolve()



# menu = open(menu_data.csv)
# type(menu_data)
# csvreader = csv.reader(menu_data)

# header_menu = next(csvreader)

# menu_rows = []
# for r in csvreader:
# 	menu_rows.append(r)

# menu_data.close()

# print(f"1st row (index 0) of menu_rows: {menu_rows[0]}")
# print(f"2nd row (index 1) of menu_rows: {menu_rows[1]}")
# print(f"data for last menu row: {menu_rows[-1]}")
# print(f"menu rows = {len(menu_rows)}")
