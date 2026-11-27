import connection as conn
import inbox
import toolKit as tk
import signIn as si
import time
def getData():
    rawData = inbox.getInboxData()
    #print("rawData: ",rawData)
    refData = rawData[6:9]              # refData stands for 'reference Data'
    #print("refData=",refData)
    finData = []
    for rec in refData:
        if "ID" in rec:
            finData.append(rec[5:])
        elif "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    finData.append('')
    #print("finData: ",finData)
    return finData
def getAdminData():
    rawData = inbox.getAdminInboxData()
    if rawData == 'err':
        inbox.createInbox([],'a')
        rawData = inbox.getAdminInboxData()
    #print("rawData: ",rawData)
    refData1 = rawData[6:9]              # refData stands for 'reference Data'
    #print("refData1: ",refData1)
    refData2 = rawData[12:15]
    #print("refData2: ",refData2)
    refData3 = rawData[18:21]
    #print("refData3: ",refData3)
    #print("refData=",refData)
    finData = []
    lstData = []
    for rec in refData1:
        if "ID" in rec:
            finData.append(rec[5:])
        elif "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    #print("finData1: ",finData)
    lstData.append(finData)
    #print("lstData1: ",lstData)
    finData = []
    for rec in refData2:
        if "ID" in rec:
            finData.append(rec[5:])
        elif "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    #print("finData2: ",finData)
    lstData.append(finData)
    #print("lstData2: ",lstData)
    finData = []
    for rec in refData3:
        if "ID" in rec:
            finData.append(rec[5:])
        elif "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    #print("finData3: ",finData)
    lstData.append(finData)
    #print("lstData3: ",lstData)
    finData = []
    return lstData

def LogInStudent(drive  = 'E:'):
    data = []
    cur = conn.connect_Server()
    if inbox.inboxExist():
        print("   \t| | fetching UserID...")
        time.sleep(0.5)
        data = getData()
        #print("data: ",data)
        print("   \t| | Data fetched successfully...")
        time.sleep(0.2)
    else:
        data = si.signInStudent(cur)
        inbox.createInbox(data,'s',drive)
        #print(data)
    print("   \t| | Uploading your ID...")
    #print(data)
    q = "INSERT INTO user_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+data[1]+"','"+data[2]+"','"+tk.getDate+"','"+tk.getTime+"');"
    #print("-----88(7243234---------------------)")
    conn.exe(q)
    print("   \t| | Upload complete...!")
    data.append(cur)
    return data

def LogInAdmin(drive = 'E:'):
    data = []
    cur = conn.connect_Server()
    if inbox.inboxExist(drive):                         # (O) To be updated, in inbox.py
        print("   \t| | Checking Admin details...")
        time.sleep(0.5)
        #print("login.py >> LogInAdmin >> data :",data)
        f = compareAdminID()
        if f[0]:
            data = f[1]
            #print("red: ",data)
        else:
            return 'den'
        print("   \t| | Data fetched successfully...")
        time.sleep(0.2)
    print("   \t| | Uploading your ID...")
    #print(data)
    q = "INSERT INTO admin_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+data[1]+"','"+data[2]+"','"+tk.getDate+"','"+tk.getTime+"');"
    conn.exe(q)
    print("   \t| | Upload complete...!")
    data.append(cur)
    return data

def compareAdminID():
    flag = False
    while not flag:
        ID = input("   \t| | Enter your ID: ")
        username = input("   \t| | Enter your username: ").upper()
        passwd = input("   \t| | Enter your password: ")
        d = [ID,username,passwd]
        data = [['1','KUNDAN GOSWAMI','kunadjo8892'],['2','DIVYANSHU JAISWAL','12345678'],['3','GUPUPREET SINGH','87654321']]
        # print("Compare data: ",data)
        if d not in data:
            print("   \t| | Wrong information!")
            print("   \t| | are you sure you are an admin?")
            print("   \t| | Try again? <y/n>")
            c = input("   \t| | -> ")
            if c[0] not in 'yY':
                return [False,[]]
        else:
            #print("Yellow : ",[ID,username,passwd])
            return [True, [ID,username,passwd]]