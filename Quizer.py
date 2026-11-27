import pickle
import random
def getQuizes(drive = 'E:'):
    data = []
    with open(drive+"\\MyQuizApp\\QUIZER\\quiz.dat",'rb') as f:
        while True:
            try:
                data.append(pickle.load(f))
            except:
                break
    return data
def getQuizRand(amt, drive = 'E:'):
    in_quizes = getQuizes(drive)
    out_quizes = []
    i=0
    while i<amt:
        try:
            r = random.randint(0,len(in_quizes)-1)
            out_quizes.append(in_quizes.pop(r))
            i+=1
        except:
            break
    return out_quizes
def addQuizes(drive = 'E:'):
    try:
        f = open(drive+"\\MyQuizApp\\QUIZER\\quiz.dat",'ab')
    except:
        f = open(drive+"\\MyQuizApp\\QUIZER\\quiz.dat",'wb')
    i = getIndex(drive)
    c = input("   \t| | Enter new Quiz? <y/n>\n->")
    quiz,op1,op2,op3,op4,c_op = '','','','','',0
    while c[0] in 'yY':
        while not quiz:
            quiz = input("   \t| | Enter your quiz: ")
        while not op1:
            op1 = input("   \t| | option 1: ")
        while not op2:
            op2 = input("   \t| | option 2: ")
        while not op3:
            op3 = input("   \t| | option 3: ")
        while not op4:
            op4 = input("   \t| | option 4: ")
        while not c_op:
            c_op = int(input("   \t| | correct option number: "))

        data = [i,quiz,op1,op2,op3,op4,c_op]
        pickle.dump(data,f)
        quiz,op1,op2,op3,op4,c_op = '','','','','',0
        i+=1
        c = input("   \t| | Enter next Quiz? <y/n>\n->")
    f.close()
    print("===============================")
    print("==QUIZZES HAVE BEEN SUBMITTED==")
    print("===============================")
def getIndex(drive = 'E:'):
    data = []
    with open(drive+"\\MyQuizApp\\QUIZER\\quiz.dat",'rb') as f:
        while True:
            try:
                data.append(pickle.load(f))
            except:
                break
    return len(data)