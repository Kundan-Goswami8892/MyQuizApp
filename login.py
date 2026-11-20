import connection as conn
import inbox
def getData():
    rawData = inbox.getInboxData()
    refData = rawData[6:9]
    finData = []
    for rec in refData:
        if "ID" in rec:
            finData.append(rec[5:])
        elif "USERNAME" in rec:
            finData.append(rec[11:])
        elif "PASSWORD" in rec:
            finData.append(rec[11:])
    return finData

'''def LogIn():
    try:
        if inbox.inboxExist():
            conn.connect_Server()
            data = getData()
            q = "INSERT INTO quizerdb.user_cadantial VALUES("+data[0]+","+data[1]+","+data[2]+","
'''