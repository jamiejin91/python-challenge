import os
import csv

ss = input("input csv file name (without .csv): ")
csvpath = os.path.join('Resources', ss + '.csv')
if not os.path.isfile(csvpath):
	print("That .csv file does not exist")
	quit()

with open(csvpath, newline='') as f:
	reader = csv.reader(f)
	data = [row for row in reader if row[0].isdigit()]
	candidates = list(set([row[2] for row in data]))
	votes = {}
	for i in range(len(candidates)):
		votes[candidates[i]] = len([ii for ii in data if ii[2] == candidates[i]])
	print("\nElection Results")
	print("-" * 50)
	print("Total Votes: {}".format(len(data)))
	print("-" * 50)
	for i in range(len(candidates)):
		print("{0}: {1:.2f}% ({2})".format(candidates[i],votes[candidates[i]]/len(data) * 100,votes[candidates[i]]))
	print("-" * 50)
	print("Winner: {}".format(list(votes.keys())[list(votes.values()).index(max([votes[i] for i in votes]))]))
	print("-" * 50)
	