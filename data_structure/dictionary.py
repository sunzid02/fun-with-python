
bag = dict()

bag['pocket_one'] = 'Dl'
bag['pocket_two'] = 'Ins'
bag['pocket_three'] = 'DC'

# print(bag)

# name count for a dictionary
counts = dict()
names = ['zia', 'zayed', 'zunayed', 'zia', 'zunayed', 'zunayed']   

# method 1
# for name in names:
#     if name in counts:
#         counts[name] = counts[name] + 1
#         # print(counts[name])
#     else:
#         counts[name] = 1


# method 2
for name in names:
    counts[name] = counts.get(name, 0 ) + 1
    # print(counts.get(name))

# print(counts)

# key print
for key in counts:
    print(key, counts[key] )


#convert dict to list and get the values
# print(list(counts))

# print( counts.keys() ) 
# print( counts.values() ) 
# print( counts.items() ) 

# two iteration variables
# for key,value in counts.items():
#     print(key, value)


# # stuff = dict()
# # print(stuff.get('candy', -11))

# # stuff = dict()
# # print(stuff['candy'])


# stuff = dict()
# print(stuff.get('candy', -1))


# stuff = dict()
# print(stuff['candy'])


stuff = dict()
print(stuff.get('candy', -1))
