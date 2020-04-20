# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, encoding='UTF-8')

hourList = list()
hourDictionary = dict()

for text in handle:
    if text.startswith('From '):
        txtSplit = text.split()
        hourTxt = txtSplit[5]
        getHourSplt = hourTxt.split(':')
        getHour = getHourSplt[0]
        hourList.append(getHour)

#count hour
for w in hourList:
    hourDictionary[w] = hourDictionary.get(w, 0) + 1

# print(hourDictionary)

# make a sorted tuple
hourTuples = sorted(hourDictionary.items())
# print(hourTuples)

for k,v in hourTuples:
    print(k, v)    
