import csv

with open('Documents/ExAmpSR/NounPEN.csv', mode='rb') as infile:
    reader = csv.reader(infile)
    nounDict = dict((rows[0],rows[1]) for rows in reader)
    # print str(nounDict).decode("string-escape")
with open('Documents/ExAmpSR/VerbPEN.csv', mode='rb') as infile:
    reader = csv.reader(infile)
    verbDict = dict((rows[0],rows[1]) for rows in reader)
    # print str(verbDict).decode("string-escape")

# resMsg = ("")
#
# elem = fromString(resMsg)
# for e in elem.findall("")

inputLine = raw_input()

polarity = 0

words = []
words.append(inputline)

for i in words:
    if words[i] in nounDict:
        word = nounDict[words[i]]
        if word == 'p':
            polarity += 1
        elif word == 'e':
            polarity += 0
        elif word == 'n':
            polarity -= 1
print polarity
