'''
In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

•Import a text file filled with a paragraph of your choosing.


•Assess the passage for each of the following:

◦Approximate word count


◦Approximate sentence count


◦Approximate letter count (per word)


◦Average sentence length (in words)



•As an example, this passage:



“Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold.”

...would yield these results:
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4

•Special Hint: You may find this code snippet helpful when determining sentence length (look into regular expressions if interested in learning more):

import re
re.split("(?&lt;=[.!?]) +", paragraph)
'''
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