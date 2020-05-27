import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.curser()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.curser()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.curser()
    cur.execute("SELECT * FROM store")
    rows=cur.fetcha11()
    conn.close()
    return rows

def delete():
    conn=sqlite3.connect("lite.db")
    cur=conn.curser()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.curser()
    cur.execute("UPDATE store SET quantity=?, price=?, WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

#update(11,6,"Water Glass")
print(view())
