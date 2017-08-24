import os
import re

txt = input("input first paragraph (without .txt): ")
txtpath = os.path.join('Resources', txt + ".txt")
if not os.path.isfile(txtpath):
	print("That .txt file does not exist")
	quit()

with open(txtpath) as file:
	data = file.read()
	data_word = re.split('\s+', data)
	data_sent = re.split('\.\s|\!\s|\?\s', data)
	data_word_clean = [i for i in data_word]
	data_sent_split = [re.split('\s+', i) for i in data_sent]
	avg_dwc = sum([len(i) for i in data_word_clean])/len(data_word_clean)
	avg_dss = sum([len(i) for i in data_sent_split])/len(data_sent_split)
	print("\nParagraph Analysis")
	print("-" * 50)
	print("Approximate Word Count: " + str(len(data_word)))
	print("Approximate Sentence Count: " + str(len(data_sent)))
	print("Average Letter Count: " + str(avg_dwc))
	print("Average Sentence Length: " + str(avg_dss) +"\n")

