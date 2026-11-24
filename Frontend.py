''' This is the main app
#
#
#
#
#
#
#
#
#
#
#
# '''
import connection as conn
import toolKit as tk
import login
import time
def appLogo():
    clr()
    print("+------------------------------------------------------------------+")
    print("|                            QUIZER                                |")
    print("|                           ````````                               |")
    print("+------------------------------------------------------------------+")
    print("\n\n")

def ScreenOne():
    appLogo()
    fetc = 100
    while fetc == 100:
        print("1  \t| | Login")
        print("   \t| |   a) Student")
        print("   \t| |   b) Admin")
        print("   \t| |   c) Moderator")
        print("2  \t| | Credits")
        print("3  \t| | Exit")
        print("...\t| | Enter your choice, (e.g. '1a' or '3').")
        c = input("Enter your choice: ")
        fetc = tk.fetchOption(c)
    if fetc == 101:
        StudentScreen(login.LogInStudent())
    elif fetc == 102:
        ''' !!!!this function is in work... !!!!'''
        #logAdminScreen(login.LogInAdmin())
    elif fetc == 103:
        ''' !!!!this function is in work... !!!!'''
        #logModeratorScreen(login.LogInMod())
    elif fetc == 200:
        creditScreen()
    elif fetc == 300:
        return "end"
    else:
        print("   \t| | =Wrong Choice=")
        clr()
        ScreenOne()
def clr():
    print("\n"*100)
def creditScreen():
    appLogo()
    print("   \t| | This project is purely made by the students of SARASWATI VIDYA MANDIR SENIOR ")
    print("   \t| | SECONDARY SCHOOL, D-1 KAMLA NAGAR, AGRA. This project is also the first and")
    print("   \t| | from 'Team Radium'.")
    print("   \t| | Staffs of TEAM RADIUM:")
    print("   \t| |\tKundan Goswami (Head Developer, Backend developer, Student of class 12th C)")
    print("   \t| |\tDivyanshu Jaiswal (Database Manager, Student of class 12th C)")
    print("   \t| |\tGurupreet Singh (Frontend developer, Interface developer, Student of class 12th C)")
    c = input("Type any key then Enter to Exit -> ")
    ScreenOne()
def StudentScreen(data):
    print("   \t| | Loading your ID...")
    time.sleep(1)
    appLogo()
    fetch = 300
    while fetch > 200 or fetch < 100:
        print("   \t| | User:- ",data[1])
        print("   \t| | ID:- ",data[0])
        print("   \t| | ")
        print("   \t| | ")
        print("1  \t| | Solve some quiz")
        print("2  \t| | Exit")
        c = input("Enter your choice: ")
        fetch = tk.fetchOption(c)
    if fetch == 100:
        SolveQuiz(data[0],data[2],data[3])
    elif fetch == 200:
        ScreenOne()

def SolveQuiz(ID,passwd,cur):
    i = 0
    while i<20:
        ''' get random quiz, assign it to a quiz variable, and blah blah blah.'''