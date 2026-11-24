import pickle
def getQuizes():
    data = []
    with open("E:\\MyQuizApp\\QUIZER\\quiz.dat",'rb') as f:
        while True:
            try:
                data.append(pickle.load(f))
            except:
                break
    return data
