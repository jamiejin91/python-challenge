import os
import csv

ss = input("input csv file name (without .csv): ")
csvpath = os.path.join('Resources', ss + '.csv')
if not os.path.isfile(csvpath):
	print("That .csv file does not exist")
	quit()

with open(csvpath, newline='') as f:
	reader = csv.reader(f)
	data = [row for row in reader if row[0] !='Date']
	month = len(data)
	monthrev = [int(i[1]) for i in data]
	revenue = sum(monthrev)
	monthavgrev = [monthrev[i+1] - monthrev[i] for i in range(month-1)]
	avgrev = sum(monthavgrev)/(month-1)
	goatinc= max(monthavgrev)
	goatdec = min(monthavgrev)
	
	print("\nFinancial Analysis")
	print("-" * 50)
	print("Total Months: {0}\nTotal Revenue: ${1}\nAverage Revenue Change: ${2:.2f}".format(month,revenue,avgrev))
	print("Greatest Increase in Revenue: {} (${})".format(data[monthavgrev.index(goatinc)+1][0],goatinc))
	print("Greatest Decrease in Revenue: {} (${})".format(data[monthavgrev.index(goatdec)+1][0],goatdec)+"\n")