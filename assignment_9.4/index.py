# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary 
# that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, 


# Desired Output
# cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, encoding='UTF-8')

dic = dict()
list = []

#create name of the email list
for txt in handle:
    if txt.startswith('From '):
        word = txt.split()
        list.append(word[1])

# print(list)


#count email sending
# method 1
for w in list:
    dic[w] = dic.get(w, 0) + 1


# method 2
# for name in list:
#     # print(name)
#     if name in dic:
#         dic[name] = dic[name] + 1
#     else:
#         dic[name] = 1

# print(dic)



#find the biggest value
biggestCount = None
biggestEmailSenderName = None

for email, count in dic.items():
    if (biggestCount is None or biggestEmailSenderName is None) or count > biggestCount:
        biggestEmailSenderName = email
        biggestCount = count

print(biggestEmailSenderName, biggestCount)
