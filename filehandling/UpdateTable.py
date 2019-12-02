import sqlite3
con = sqlite3.connect('example.db')


def sql_update(con):
    cursorObj = con.cursor()
    symbol = 'Ram'
    cursorObj.execute("UPDATE employee SET address = 'HCL 126 noida' where name = '%s'" % symbol)
    con.commit()


sql_update(con)
c = con.cursor()
c.execute("SELECT * FROM employee where name='Ram' ")
print(c.fetchall())