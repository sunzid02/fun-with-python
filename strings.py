

# word = 'hello there'

# print( word[5:] )

# #in used to check that, if e is found in word variable
# a = 'e' in word
# print(a)

# print( word.upper() )
# print( word )

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(pos)
# print(data[pos:pos+3])


# #removing whitespaces
# word = ' he '
# remWord = word.strip()
# print(word)
# print(remWord)


# How would you use string slicing [:] to print out 'uct' from the following string?
x = 'From marquard@uct.ac.za'
startPos = x.find('@')
print(startPos)
endPos = x.find('.', startPos)
print(endPos)

desiredString = x[ startPos+1 : endPos ]
print(desiredString)