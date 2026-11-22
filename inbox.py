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
    if Path("C:\\Program Files\\QUIZER").exists():
        flag_new_install = False
        # flag_Recreate_indox = False
        # flag_Recreate_indox_dat = False
        if Path("C:\\Program Files\\QUIZER\\inbox").exists():
            flag_Recreate_indox = False
            if Path("C:\\Program Files\\QUIZER\\inbox\\inbox.dat").exists():
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

def createInbox(data):
    if flag_new_install:
        Path("C:\\Program Files\\QUIZER").mkdir()
    if flag_Recreate_indox:
        Path("C:\\Program Files\\QUIZER\\inbox").mkdir()
    if flag_Recreate_indox_dat:
        inbox = open("C:\\Program Files\\QUIZER\\inbox\\inbox.dat",'wb',newline='')
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

def getInbox():
    try:
        if not flag_Recreate_indox_dat:
            f = open("C:\\Program Files\\QUIZER\\inbox\\inbox.dat")
            return f
        return "nidx"           # 'nidx' means 'no index'
    except:
        print("error in inbox.py, line 60")
        return "err"            # this means error.
def getInboxData():
    try:
        if not flag_Recreate_indox_dat:
            f = open("C:\\Program Files\\QUIZER\\inbox\\inbox.dat")
            return f.read()
        return "nidx"
    except:
        return "err"
def enterData(data):
    d = getInboxData()
    d[6] = "ID : "+str(data[0])
    d[7] = "USERNAME : "+str(data[1])
    d[8] = "PASSWORD : "+str(data[2])