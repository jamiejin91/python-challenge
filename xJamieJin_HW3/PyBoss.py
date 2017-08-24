import os
import csv

ss = input("input csv file name (without .csv): ")
csvpath = os.path.join('Resources', ss + '.csv')
if not os.path.isfile(csvpath):
	print("That .csv file does not exist")
	quit()

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csvpath, newline='') as f:
	reader = csv.reader(f)
	data = [row for row in reader if row[0] !='Emp ID']
	names = [i[1].split(" ") for i in data]
	first = [i[0] for i in names]
	last = [i[1] for i in names]
	dob = ["/".join(i[2].split("-")) for i in data]
	ssn = ["***-**-{}".format(i[3][7:len(i[3])]) for i in data]
	states = [us_state_abbrev[i[4]] for i in data]
	final = zip([i[0] for i in data],first,last,dob,ssn,states)

ssout = input("input output csv name (without .csv): ")
with open(ssout + '.csv', 'w', newline = '') as ff:
	writer = csv.writer(ff, delimiter=",")
	writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
	for i in final:
		writer.writerow(i)

print("Please find {}.csv in folder {}".format(ssout,os.path.dirname(os.path.realpath(__file__))))