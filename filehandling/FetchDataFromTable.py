import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

symbol = 'Krishan'
c.execute("SELECT * FROM employee WHERE name = '%s'" % symbol)
print(c.fetchall())

#Larger example that inserts many records at a time
employees = [('1133', 'abc@abc.com', 'Ramesh', 'Sector 11'),
             ('1134', 'abc@abc.com', 'Shyam', 'Sector 12'),
             ('1135', 'abc@abc.com', 'Gita', 'Sector 22'),
            ]
c.executemany('INSERT INTO employee VALUES (?,?,?,?)', employees)

for row in c.execute('SELECT * FROM employee ORDER BY name'):
    print(row)

