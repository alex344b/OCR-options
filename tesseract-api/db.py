import sqlite3

con = sqlite3.connect('receipt.db', check_same_thread=False)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS invoce(file VARCHAR(255), content MEDIUMTEXT)')


def insertText(file, context):
    cur.execute('INSERT INTO invoce VALUES(?, ?)', (file, context, ))


def selectAll():
    return cur.execute('SELECT rowid, file, content FROM invoce').fetchall()
