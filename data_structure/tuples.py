
# sorting tuples
d = { 'a': 1, 'b': 10, 'c': 22}
# print(d)
# print( d.items() )#make dic a list of tuples

sd = sorted( d.items() )
# print(sd)

# sortby value instead of key
dic = { 'a': 1, 'b': 10, 'c': 22 }

tmp = list()

for k, v in dic.items():
    tmp.append( (v,k) )
print(tmp)
tmp = sorted( tmp, reverse=True )
print(tmp)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])