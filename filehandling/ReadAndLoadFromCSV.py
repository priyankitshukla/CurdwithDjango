import sqlite3
import csv

conn = sqlite3.connect('example.db')
c = conn.cursor()

#Create table
c.execute('''CREATE TABLE employee
             (id integer PRIMARY KEY,
                email text,
                name text,
                address text)''')

with open('employee.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        print(row)
        c.execute("INSERT INTO employee VALUES (?, ?, ?, ?)", row)
conn.commit()
# rows = c.execute("SELECT * FROM employee ")
# print(rows.fetchall())