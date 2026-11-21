import connection as conn
import inbox
import toolKit as tk
import signIn as si
def getData():
    rawData = inbox.getInboxData()
    refData = rawData[6:9]
    finData = []
    for rec in refData:
        if "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    return finData


def LogIn():
    try:
        cur = conn.connect_Server()
        if inbox.inboxExist():
            data = getData()
        else:
            inbox.createInbox()
            data = si.signIn(cur)
        
        q = "INSERT INTO user_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+data[0]+"','"+data[1]+"','"+tk.getDate+"','"+tk.getTime+"');"
        conn.exe(q)
    except:
        print("error in login.py, at line 29")
        