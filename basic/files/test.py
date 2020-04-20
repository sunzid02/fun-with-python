
# opening the file
fhandle = open( 'test.txt' )
# print(fhandle)

# read the file
for file in fhandle:
    print(file)

#line count from the file
count = 0
fhandle = open( 'test.txt' )

for lineCount in fhandle:
    count = count + 1
    
print('Total ' , count , 'lines inside this file')
