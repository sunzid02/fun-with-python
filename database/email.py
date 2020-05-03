import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
    CREATE TABLE Counts (email TEXT, count INTEGER)
''')

fname = input('Enter file name: ')
if( len(fname) < 1 ): fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    # print(pieces[1])
    email = pieces[1]
    cur.execute('SELECT count from Counts where email = ?', (email,) )
    row = cur.fetchone() #grab the first one
    print(row)
    if row is None:
        cur.execute('''INSERT into Counts (email, count)
        values (?, 1)''', (email,))
    else:
        cur.execute('update Counts set count = count + 1 where email = ?', (email,))
    conn.commit()

# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1] )
