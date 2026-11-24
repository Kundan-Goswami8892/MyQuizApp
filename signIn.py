# import connection as conn
import toolKit as tk
def fetchSQLdata(cur):
    cur.execute("SELECT user_ID,username,passwd FROM user_cadantial;")
    data =[]
    for i in cur:
        data.append(i)
    return data
def signInStudent(cur):
    
    username = input("Enter your Username: ")
    passwd = input("Enter your Password: ")
    try:
        cur.execute("INSERT INTO user_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+username+"','"+passwd+"','"+tk.getDate+"','"+tk.getTime+"');")
    except:
        print("error in signIn.py, at line 16")
        data = []
        return data
    data = fetchSQLdata(cur)
    return data
