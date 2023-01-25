import sqlite3
import time


# db생성
# conn = sqlite3.connect('blog.db')
#
# c = conn.cursor()
# 데이터 생성
# query = '''CREATE TABLE blog (ID INTEGER PRIMARY KEY, subject text, content text, date text)'''
# c.execute(query)
# c.execute("INSERT INTO blog VALUES (1, '첫 번째 블로그', '첫 번째 작성글입니다.', '20221022')")
# conn.commit()
# c.execute("INSERT INTO blog VALUES (2, '두 번째 블로그', '두 번째 작성글입니다.', '20221022')")
# conn.commit()
# c.execute("INSERT INTO blog VALUES (3, '세 번째 블로그', '세 번째 작성글입니다.', '20221022')")
# conn.commit()
# c.execute('SELECT * FROM blog')
# all = c.fetchall()
# conn.close()
# print(all)

# 블로그 전체 보기
def get_blog_list():
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("SELECT * FROM blog")
    result = c.fetchall()
    conn.close()
    return result

# 신규 블로그 작성 함수
def add_blog(subject, content):
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    today = time.strftime('%Y%m%d')
    c.execute("insert into blog (subject, content, date) VALUES (?,?,?)", (subject,content,today))
    conn.commit()
    conn.close()

# 블로그 1개만 읽기
def read_blog(_id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM blog WHERE id=?", (_id,))
    result = c.fetchone()
    conn.close()
    return result

# 블로그 수정
def modify_blog(_id, subject, content):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE blog SET subject=?, content=? WHERE id=?",
        (subject, content, _id))
    conn.commit()
    conn.close()

def remove_blog(_id):
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("DELETE FROM blog WHERE id=?", (_id,))
    conn.commit()
    conn.close()

