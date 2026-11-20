import mysql.connector as ms

''' this methode is made here, so that we can connect to database more easily without writing 
    a whole mess over and over.'''
def connect_Server():                   
    global conn
    global i
    i=0
    conn = ms.connect(host="localhost",user='root',passwd='root',database='quizerDB')
    global cur
    cur = conn.connect()
    return cur               # we might need to abstract the cursor out, so... just in case:)

''' This function here is a replacement of the cursor object.'''
def exe(query):
    try:
        cur.execute(query)
        i+=1
        if i>=5:
            conn.commit()
            i=0
    except:
        return False
    return True

'''This fuction simply just closes the connection object and cursor object'''
def close():
    conn.close()
    cur.close()