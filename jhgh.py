
import sqlite3
import csv
i=csv.reader(open('qidian.csv'))
i=list(i)[1:]
print(i)
l=['科幻', '都市', '悬疑', '玄幻', '军事', '奇幻', '历史', '仙侠', '百合', '游戏']
# l=['完结','连载']
for j in l:
    # name=list(i)[j][0]
    # href=list(i)[j][2]
    # author=list(i)[j][1]
    # count= list(i)[j][5]
    # img="static/bookimg/%d.jpg"%j
    # book_intro=list(i)[j][-1]
    # print(name,href,author,count,img,book_intro)
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    # cur.execute("insert into novel_novel (name,href,author,count,img,book_intro) values ('%s','%s','%s','%s','%s','%s')"%(name,href,author,count,img,book_intro))
    # conn.commit()
    cur.execute("insert into BookTitle(title) values ('%s')" % (j))
    results = cur.fetchall()


    conn.commit()

    cur.close()

    conn.close()
