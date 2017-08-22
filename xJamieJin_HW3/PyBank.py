import csv
ss = input("input first csv file (without .csv): ") + ".csv"

with open(ss, newline='') as f:
	reader = csv.reader(f)
	data = [row for row in reader if row[0] !='Date' and row[1].isdigit()]
	month = len(data)
	monthrev = [int(_[1]) for _ in data]
	revenue = sum(monthrev)
	monthavgrev = [monthrev[i+1] - monthrev[i] for i in range(month-1)]
	avgrev = sum(monthavgrev)/(month-1)
	goatinc= max(monthavgrev)
	goatdec = min(monthavgrev)
	print("\n\nFinancial Analysis")
	print("-" * 50)
	print("Total Months: {0}\nTotal Revenue: ${1}\nAverage Revenue Change: ${2:.2f}".format(month,revenue,avgrev))
	print("Greatest Increase in Revenue: {} (${})".format("ayy",goatinc))
	print("Greatest Decrease in Revenue: {} (${})\n\n".format("lmao",goatdec))

''' Question: goat increase/decrease display?'''