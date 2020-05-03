import sqlite3




fname = input('Enter file name: ')
if(len(fname) < 1):
    fname = 'mbox.txt'

fh = open(fname)
emailList = list()
dic = dict()

for line in fh:
    if( line.startswith('From: ') ):
        pieces = line.split()
        email = pieces[1]

        secPc =  email.split('@')
        orgN = secPc[1]

        emailList.append(orgN)
    else:
        continue
    
# print(emailList)


#count email sending
for email in emailList:
    dic[email] = dic.get(email, 0) + 1

# print(dic)



conn = sqlite3.connect('assignmentdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)
''')


## email insert
for email, count in dic.items():
    # print(email, count)
    cur.execute('''INSERT into Counts (org, count) values (?, ?)''', (email, count))
    conn.commit()




sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'


print(cur.execute(sqlstr))
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])






#     email = pieces[1]
#     cur.execute('SELECT count from Counts where email = ?', (email,))

#     row = cur.fetchone()  # grab the first one
#     if row is None:
#         cur.execute('''INSERT into Counts (email, count)
#         values (?, 1)''', (email,))
#     else:
#         cur.execute(
#             'update Counts set count = count + 1 where email = ?', (email,))
#     conn.commit()

# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
