import re
txt = input("input first paragraph (without .txt): ") + ".txt"

with open(txt) as file:
	data = file.read()
	data_sent = re.split(r'(?<=\.) ', data)
	data_word = re.split('\s+', data)
	regex = re.compile('[^a-zA-Z]')
	data_word_clean = [regex.sub('', i) for i in data_word]
	data_sent_split = [[ii.split(" ") for ii in data_sent[i]] for i in range(len(data_sent))]
	avg_dwc = sum([len(i) for i in data_word_clean])/len(data_word_clean)
	avg_dss = sum([len(i) for i in data_sent_split])/len(data_sent_split)
	for i in range(len(data_sent)):
		print(str(i) + data_sent[i])
	for ii in range(len(data_word)):
		print(str(ii)+ data_word[ii])
	'''print("\n\nParagraph Analysis")
	print("-" * 50)
	print("Approximate Word Count: " + str(len(data_word)))
	print("Approximate Sentence Count: " + str(len(data_sent)))
	print("Average Letter Count: " + str(avg_dwc))
	print("Average Sentence Length: " + str(avg_dss) +"\n\n")'''