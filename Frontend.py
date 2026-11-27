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
def end():
    conn.close()
    print("X----------------------------------------------------X")
    print("X----------------------------------------------------X")
    print("X----------------------------------------------------X")
    print("X----------------------------------------------------X")

    
def ScreenOne(drive = 'E:'):
    appLogo()
    flag=True
    while flag:
        print("1  \t| | Login")
        print("   \t| |   a) Student")
        print("   \t| |   b) Admin")
        print("2  \t| | Credits")
        print("3  \t| | Exit")
        print("...\t| | Enter your choice, (e.g. '1a' or '2').")
        c = input("   \t| | Enter your choice: ")
        c = c.lower()
        if c == '1a':
            StudentScreen(login.LogInStudent(drive))
        elif c == '1b':
            AdminScreen(login.LogInAdmin(drive))
        elif c == '2':
            creditScreen()
        elif c == '3':
            flag = False
            end()
            return flag
        else:
            print("   \t| | =Wrong Choice=")
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
    c = input("   \t| | Type any key then Enter to Exit -> ")
    return
def StudentScreen(data, drive = 'E:'):
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
        c = input("   \t| | Enter your choice: ")
        if c == '1':
            print("=> \t| | SOLVE SOME QUIZES")
            print("   \t| | ")
            print("   \t| | ")
            print("   \t| | ",data[3])
            SolveQuiz(data, drive = 'E:')
        elif c == '2':
            return
def AdminScreen(data,drive = 'E:'):
    if data == 'den':
        return
    print("   \t| | Loading your ID...")
    time.sleep(1)
    appLogo()
    while True:
        print("   \t| | User:- ",data[1])
        print("   \t| | ID:- ",data[0])
        print("   \t| | ")
        print("   \t| | ")
        print("1  \t| | Add some quiz")
        print("2  \t| | Exit")
        c = input("Enter your choice: ")
        if c == '1':
            print("=> \t| | ADD SOME QUIZES")
            print("   \t| | ")
            print("   \t| | ")
            print("   \t| | ")
            Quizer.addQuizes(drive)
        elif c == '2':
            return
def SolveQuiz(data, drive = 'E:'):
    i = 1
    sc = 0
    quizi = Quizer.getQuizRand(20, drive)
    for quiz in quizi:
        print(i,"  \t| |",quiz[1])
        print("   \t| | 1) ",quiz[2])
        print("   \t| | 2) ",quiz[3])
        print("   \t| | 3) ",quiz[4])
        print("   \t| | 4) ",quiz[5])
        c = int(input("   \t| | -> "))
        if c == quiz[6]:
            sc += 1
    if sc <= 5:
        msg = "   \t| | === Awwww... Better luck next time:) "
    elif sc <=10:
        msg ="   \t| | === At least you tried."
    elif sc <=15:
        msg = "   \t| | === Quite average."
    elif sc<=18:
        msg = "   \t| | === Ohhh!!!! NICEE!!!"
    elif sc == 19:
        msg = "   \t| | === OFF BY 1 POINT?!!! "
    elif sc == 20:
        msg = "   \t| | === OMG!! THAT's A PERFECT SCORE!!!"
    print(msg)
    data[3] = str(sc)+msg
    StudentScreen(data, drive)