import mysql.connector as ms
def connect_Server():
    global conn
    conn = ms.connect(host="localhost",user='root',passwd='root',database='quizerDB')
    global cur
    cur = conn.connect()
    return cur

def exe(query):
    try:
        cur.execute(query)
        conn.commit()
    except:
        return False
    return True
def close():
    conn.close()
    cur.close()