tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def PrintTable(lis):
    count = 0
    while count <= (len(lis)):
            for x in range(len(lis)):
                print (lis[count][x], end = "/n")
                count += 1

PrintTable(tableData)