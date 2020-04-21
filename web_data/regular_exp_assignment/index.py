# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers.
# Actual data: http: // py4e-data.dr-chuck.net/regex_sum_423413.txt(There are 63 values and the sum ends with 626)

import re

file = open('regex_sum_423413.txt')
numbers = list()
count = 0
sum = 0

for fh in file:
    numberExp = re.findall( '[0-9]+', fh ) #extracting the number
    if len(numberExp) == 0:
        continue
    else:
        
        if len(numberExp) == 1:
            sum = sum + int( numberExp[0] )
            count = count + 1

        else:
            for num in numberExp:
                sum = sum + int(num)
                count = count + 1


        # numbers.append(numberExp)

# print(count)
print(sum)
# print(numbers)
