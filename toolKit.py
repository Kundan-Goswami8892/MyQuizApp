from datetime import datetime
getDate = datetime.now().strftime("%d-%m-%Y")
getTime = datetime.now().strftime("%H:%M:%S")
def fetchOption(op):
    op = op.lower()
    fetcher = int(op[0])
    if len(op) > 1:
        for i in range(1, len(op)+1):
            fetcher = fetcher*100 + (ord(op[i]) - 96)
    return fetcher
