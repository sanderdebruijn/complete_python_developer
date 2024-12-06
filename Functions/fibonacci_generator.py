

def fibon(num):
    nmin = 0
    nmin2 = 0
    for i in range(0, num+1):
        n = nmin + nmin2
        yield n
        if i == 0:
            nmin2 = 1
        else:
            nmin2 = nmin
            nmin = n


for i in fibon(20):
    print(i)
