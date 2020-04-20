# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the 
# average of those values and produce an output as shown below. Do not use the summation() function or a 
# variable named quantity in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing 
# below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

lineCount = 0
quantity = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        findColon = line.find(':')
        startPos = line.find('0', findColon)

        string = line[startPos:]
        number = float(string)
        
        lineCount = lineCount + 1
        quantity = quantity + number


avg = quantity / lineCount

print('Average spam confidence:', avg)

