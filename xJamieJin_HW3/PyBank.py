'''
In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data ( budget_data_1.csv  and  budget_data_2.csv ). Each dataset is composed of two columns:  Date  and  Revenue . (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

•The total number of months included in the dataset


•The total amount of revenue gained over the entire period


•The average change in revenue between months over the entire period


•The greatest increase in revenue (date and amount) over the entire period


•The greatest decrease in revenue (date and amount) over the entire period


As an example, your analysis should look similar to the one below:
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)


Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''


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