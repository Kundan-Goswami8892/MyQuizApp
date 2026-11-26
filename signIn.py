# import connection as conn
import toolKit as tk
def fetchSQLdata(cur):
    cur.execute("SELECT user_ID,username,passwd FROM user_cadantial ORDER BY user_ID DESC;")
    data = list(list(cur)[0])
    return data
def signInStudent(cur):
    
    username = input("   \t| | Enter your Username: ")
    passwd = input("   \t| | Enter your Password: ")
    try:
        #print("------SignIn.py before cursor--------------------------------")
        cur.execute("INSERT INTO user_cadantial(username,passwd,sign_up_date,sign_up_time) VALUES('"+username+"','"+passwd+"','"+tk.getDate+"','"+tk.getTime+"');")
        #print("------SignIn.py after cursor--------------------------------")
    except:
        print("error in signIn.py, at line 16")
        data = []
        return data
    #print("fetching data-------------------------------")
    data = fetchSQLdata(cur)
    #print("data fetched--------------------------------")
    return data

