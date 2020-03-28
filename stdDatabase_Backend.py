import sqlite3
#backend

def contactData():
    con=sqlite3.connect("Contacts.db")
    cur = con.cursor()
    cur.execute("Create TABLE IF NOT EXISTS contact(id INTEGER PRIMARY KEY, Fname text, Mname text, Lname text, \
                Mail text, Mnumber text, Wnumber text, Dob text)")
    con.commit()
    con.close()

def addConRec(fname, mname, lname, mail, mnumb, wnumber, dob):
    con = sqlite3.connect("Contacts.db")
    cur = con.cursor()
    cur.execute("INSERT INTO contact VALUES (NULL, ?,?,?,?,?,?,?)", (fname, mname, lname, mail, mnumb, wnumber, dob))
    con.commit()
    con.close()


def viewDate():
    con = sqlite3.connect("Contacts.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM contact")
    row= cur.fetchall()
    con.close()
    return row

def deleteRec(id):
    con = sqlite3.connect("Contacts.db")
    cur =con.cursor()
    cur.execute("DELETE FROM contact WHERE id=?",(id,))
    con.commit()
    con.close()


def dataUpdate(fname="", mname="", lname="", mail="", mnumb="", wnumber="", dob=""):
    con = sqlite3.connect("Contacts.db")
    cur =con.cursor()
    cur.execute("UPDATE contact SET fname=?, OR mname=?, OR lname=?, OR mail=?, OR mnumb=?, OR wnumb=?, OR dob=?",
                (fname, mname, lname, mail, mnumb, wnumber, dob))
    con.commit()
    con.close()



contactData()