import random
numberOfStreaks = 0
RowCount = 0
for experimentNumber in range(10000):
    Flips = [] 
    for x in range(100): 
        flip = random.randint(0,1)
        if flip == 1:
            Flips.append("H")
        elif flip ==  0:
            Flips.append("T")

    for i  in range(len(Flips)):
        if Flips[i] == Flips[i-1]:
            RowCount += 1
            if RowCount == 6:
                numberOfStreaks += 1
                RowCount == 0
        else:
            RowCount = 0
       


print('Chance of streak: %s%%' % (numberOfStreaks / 100))