import re

# x = 'my 2 favourite numbers are 19 aand 45 '

# #it will run like: [0-9] any char from 0 to 9, + repeat one or more charecters
# y = re.findall( '.+' , x )
# # y = re.findall( '^m.+1' , x )
# print(y)


# mailWord = 'From sunzid02@gmail.com yahoo!'
# # mailWord = 'my email is sunzid02@gmail.com yahoo!'
# # email = re.findall( '^From (\S+@\S+)', mailWord )
# # email = re.findall( '\S+@\S+', mailWord )

# # domain = re.findall('@([^ ]+)', mailWord)  # [^ ]* means nonblank charecters 0 or more times
# # [^ ]* means nonblank charecters 0 or more times
# domain = re.findall('[a-z0-9]', mailWord)




# print(domain)


# x = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
# y = re.findall('href="(.+)"', x)
# print(y)

# print(repeating_letter_a("banana"))  # True
# print(repeating_letter_a("pineapple"))  # False
# print(repeating_letter_a("Animal Kingdom"))  # True
# print(repeating_letter_a("A is for apple"))  # True


str = 'banaana'
# str = 'aaDaaa'

# res = re.findall('[pa+]', str)
res = re.findall(r'[aA].*[aA]', str)
# # res = re.search(r'.*\s*[aA].*\s*[aA].*', str)
# res = re.findall(r'.*\s*[aA].*\s*[aA].*', str)
# res = re.findall(r'[aA].*?[aA]', str)

print(res)


# matches = re.findall(r'((.)\2+)', 'baanana')

# print(matches)


newStr = 'elphant'

matches2 = re.findall('[^ph]', newStr)
print(matches2)
