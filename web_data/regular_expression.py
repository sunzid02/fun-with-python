import re

x = 'my 2 favourite numbers are 19 aand 45 '

#it will run like: [0-9] any char from 0 to 9, + repeat one or more charecters
y = re.findall( '\S.+e\S' , x )
# y = re.findall( '^m.+1' , x )
print(y)


mailWord = 'From sunzid02@gmail.com yahoo!'
# mailWord = 'my email is sunzid02@gmail.com yahoo!'
# email = re.findall( '^From (\S+@\S+)', mailWord )
# email = re.findall( '\S+@\S+', mailWord )

# domain = re.findall('@([^ ]+)', mailWord)  # [^ ]* means nonblank charecters 0 or more times
# [^ ]* means nonblank charecters 0 or more times
domain = re.findall('[a-z0-9]', mailWord)




print(domain)


x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)
