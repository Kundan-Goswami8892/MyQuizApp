import mysql.connector as ms

''' this methode is made here, so that we can connect to database more easily without writing 
    a whole mess over and over.'''
def connect_Server():                   
    global conn
    conn = ms.connect(host="localhost",user='root',passwd='root')
    global cur
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS quizerdb;")
    cur.execute("USE quizerdb;")
    cur.execute("CREATE TABLE IF NOT EXISTS user_cadantial(user_ID bigint primary key,username varchar(20),passwd varchar(16), sign_up_date varchar(10),sign_up_time varchar(10));")
    conn.commit()
    return cur               # we might need to abstract the cursor out, so... just in case:)

''' This function here is a replacement of the cursor object.'''
def exe(query):
    try:
        cur.execute(query)
        conn.commit()
    except:
        print("Error at Connection.py, line 22.")
        return False
    return True

'''This fuction simply just closes the connection object and cursor object'''
def close():
    conn.close()
    cur.close()