
import sqlite3
for i in range(1,51):
    img="static/img/%d.jpg"%i
    # j=int(48+i)
    conn = sqlite3.connect('db.sqlite3')

    cur = conn.cursor()

    cur.execute("insert into app_reinr values (%d,%d,'%s')"%(i,i,img))
    # conn.commit()
    results = cur.fetchall()


    conn.commit()

    cur.close()

    conn.close()
