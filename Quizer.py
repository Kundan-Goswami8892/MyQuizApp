import pickle
import random
def getQuizes():
    data = []
    with open("E:\\MyQuizApp\\QUIZER\\quiz.dat",'rb') as f:
        while True:
            try:
                data.append(pickle.load(f))
                print(data)
            except:
                break
    return data
def getQuizRand(amt):
    in_quizes = getQuizes()
    out_quizes = []
    i=0
    while i<amt:
        r = random.randint(0,len(in_quizes)-1)
        out_quizes.append(in_quizes.pop(i))
    return out_quizes