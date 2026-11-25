import connection as conn
import inbox
import toolKit as tk
import signIn as si
import time
def getData():
    rawData = inbox.getInboxData()
    refData = rawData[0][6:9]              # refData stands for 'reference Data'
    #print("refData=",refData)
    finData = []
    for rec in refData:
        if "ID" in rec:
            finData.append(rec[5:])
        elif "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    #print(finData)
    return finData

'''
def LogInStudent():
    data = []
    try:
        cur = conn.connect_Server()
        if inbox.inboxExist() and inbox.hasData():
            print("   \t| | fetching UserID...")
            time.sleep(0.5)
            data = getData()
            print("   \t| | Data fetched successfully...")
            time.sleep(0.2)
        else:
            data = si.signInStudent(cur)
            #print("-------2353456435643-56435--------------------")
            inbox.createInbox(data)
        print("   \t| | Uploading your ID...")
        q = "INSERT INTO user_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+data[0]+"','"+data[1]+"','"+tk.getDate+"','"+tk.getTime+"');"
        print("-----88(7243234---------------------)")
        conn.exe(q)
        print("   \t| | Upload complete...!")
    except :
        print("error in login.py, at line 35")
        return data
    data.append(cur)
    return data
'''
def LogInStudent():
    data = []
    cur = conn.connect_Server()
    if inbox.inboxExist():
        print("   \t| | fetching UserID...")
        time.sleep(0.5)
        data = getData()
        #print(data)
        print("   \t| | Data fetched successfully...")
        time.sleep(0.2)
    else:
        data = si.signInStudent(cur)
        inbox.createInbox(data)
        print(data)
    print("   \t| | Uploading your ID...")
    #print(data)
    q = "INSERT INTO user_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+data[1]+"','"+data[2]+"','"+tk.getDate+"','"+tk.getTime+"');"
    #print("-----88(7243234---------------------)")
    conn.exe(q)
    print("   \t| | Upload complete...!")
    data.append(cur)
    return data
