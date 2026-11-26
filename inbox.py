import pickle as p
from pathlib import Path
import connection as conn

flag_new_install = False
flag_Recreate_indox = False
flag_Recreate_indox_dat = False
def inboxExist():
    global flag_new_install
    global flag_Recreate_indox
    global flag_Recreate_indox_dat
    if Path("E:\\MyQuizApp\\QUIZER").exists():
        flag_new_install = False
        # flag_Recreate_indox = False
        # flag_Recreate_indox_dat = False
        if Path("E:\\MyQuizApp\\QUIZER\\inbox").exists():
            flag_Recreate_indox = False
            if Path("E:\\MyQuizApp\\QUIZER\\inbox\\inbox.dat").exists():
                flag_Recreate_indox_dat = False
                return True
            else:
                flag_Recreate_indox_dat = True
                return False
        else:
            flag_Recreate_indox = True
            return False
    else:
        flag_new_install = True
        return False

def createInbox(data,mode):
    if flag_new_install:
        Path("E:\\MyQuizApp\\QUIZER").mkdir()
    if flag_Recreate_indox:
        Path("E:\\MyQuizApp\\QUIZER\\inbox").mkdir()
    if mode.lower() == 's':
        inbox = open("E:\\MyQuizApp\\QUIZER\\inbox\\inbox.dat",'wb')
        p.dump(["X-------------------QUIZER-------------------X",
                "\n",
                "\n",
                "USER CADANTIAL--------------------->>>",
                "\n",
                "\n",
                "ID : "+str(data[0]),                 #6
                "USERNAME : "+str(data[1]),           #7
                "PASSWORD : "+str(data[2]),           #8
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>"],
                inbox)
        inbox.close()
    elif mode.lower() == 'a':
        inbox = open("E:\\MyQuizApp\\QUIZER\\inbox\\admininbox.dat",'wb')
        p.dump(["X-------------------QUIZER-------------------X",
                "\n",
                "\n",
                "USER CADANTIAL--------------------->>>",
                "\n",
                "\n",
                "ID : 1",                 #6
                "USERNAME : KUNDAN GOSWAMI",           #7
                "PASSWORD : kunadjo8892",           #8
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>",
                "ID : 2",                 #12
                "USERNAME : DIVYANSHU JAISWAL",           #13
                "PASSWORD : 12345678",           #14
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>",
                "ID : 3",                 #18
                "USERNAME : GUPUPREET SINGH",           #19
                "PASSWORD : 87654321",           #20
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>",
                "<<<--------------------------------------------------------->>>"],
                inbox)
        inbox.close()

def getInbox():
    try:
        if not flag_Recreate_indox_dat:
            f = open("E:\\MyQuizApp\\QUIZER\\inbox\\inbox.dat")
            return f
        return "nidx"           # 'nidx' means 'no index'
    except:
        print("error in inbox.py, line 60")
        return "err"            # this means error.
def getInboxData():
    try:
        if not flag_Recreate_indox_dat:
            f = open("E:\\MyQuizApp\\QUIZER\\inbox\\inbox.dat",'rb')
            data = p.load(f)
            return data
    except:
        return "err"
def getAdminInboxData():
    if Path("E:\\MyQuizApp\\QUIZER\\inbox\\admininbox.dat").exists():
        f = open("E:\\MyQuizApp\\QUIZER\\inbox\\admininbox.dat",'rb')
    else:
        createInbox([],'a')
        f = open("E:\\MyQuizApp\\QUIZER\\inbox\\admininbox.dat",'rb')
    data= p.load(f)
    return data
    
def enterData(data):
    d = getInboxData()
    d[6] = "ID : "+str(data[0])
    d[7] = "USERNAME : "+str(data[1])
    d[8] = "PASSWORD : "+str(data[2])
    createInbox(d,'s')
def hasData():
    data = getInboxData()
    if data[6] == 'ID : ':
        return False
    return True
