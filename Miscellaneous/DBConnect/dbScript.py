import sqlite3

def createTable():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS STORE (item TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()
    print("Connection Closed")


def insert(item,qty,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    ##cur.execute("INSERT INTO Store VALUES('Wine Glass',8,10.5)")
    cur.execute("INSERT INTO Store VALUES(?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()

def delItem(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("delete from Store where item = ?",(item,))
    conn.commit()
    conn.close()

def updItem(item,qty,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("update Store set quantity = ? , price = ? where item = ?",(qty,price,item))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("select * from Store")
    rows=cur.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    #initDb()
    delItem("Bolt")
    delItem("Cofee Cup")
    delItem("Wine Glass")
    insert("Cofee Cup", 10, 5)
    insert("Bolt",10,2)
    insert('Wine Glass', 8, 10.5)
    updItem('Wine Glass', 500, 100)
    print(view())
