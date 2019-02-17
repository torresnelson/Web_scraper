words = []
f = open('DICTIONARY.csv','r')
for i in range(527803):
	words.append(str(f.readline()))
f.close()
word = words[0].split()
for i in range (527803):
	target = word[0]
	print(target)
	word = words[i].split()