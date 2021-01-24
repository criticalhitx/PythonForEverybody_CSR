import sqlite3

conn = sqlite3.connect('examdb.sqlite') #Name of DB, will be create if not existed
cur = conn.cursor() #Handler

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname)<1 : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    x = email.split('@')
    org = x[1]
    print(org)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,)) # Cek apakah sudah ada entry atau belum
    row = cur.fetchone() # Cek apakah sudah ada entry atau belum
    if row is None : 
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()

#Read the DB
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' #limit by 10 entry, sort from highest count

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1]) #row 0 is email, row 1 is count

cur.close()