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
import Quizer
def appLogo():
    clr()
    print("+------------------------------------------------------------------+")
    print("|                            QUIZER                                |")
    print("|                           ````````                               |")
    print("+------------------------------------------------------------------+")
    print("\n\n")

def ScreenOne():
    appLogo()
    flag=True
    while flag:
        print("1  \t| | Login")
        print("   \t| |   a) Student")
        print("   \t| |   b) Admin")
        print("2  \t| | Credits")
        print("3  \t| | Exit")
        print("...\t| | Enter your choice, (e.g. '1a' or '2').")
        c = input("Enter your choice: ").lower()
        if c == '1a':
            StudentScreen(login.LogInStudent())
        elif c == '1b':
            ''' !!!!this function is in work... !!!!'''
            #logAdminScreen(login.LogInAdmin())
        elif c == '2':
            creditScreen()
        elif c == '3':
            flag = False
            return flag
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
    while True:
        print("   \t| | User:- ",data[1])
        print("   \t| | ID:- ",data[0])
        print("   \t| | ")
        print("   \t| | ")
        print("1  \t| | Solve some quiz")
        print("2  \t| | Exit")
        c = input("Enter your choice: ")
        if c == '1':
            print("=> \t| | SOLVE SOME QUIZES")
            print("   \t| | ")
            print("   \t| | ")
            print("   \t| | ")
            SolveQuiz(data[0],data[2],data[3])
        elif c == '2':
            ScreenOne()

def SolveQuiz(ID,passwd,cur):
    i = 1
    quizi = Quizer.getQuizRand(20)
    for quiz in quizi:
        print(i,"  \t| |",quiz)