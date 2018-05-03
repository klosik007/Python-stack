def printTable(table):
    colWidhts = [0] * len(table)
    cTable = table
    for i in range(len(cTable)):
        cTable[i].sort(key=len)
        #print(cTable)
        colWidhts[i] = len(cTable[i][len(table[i])-1])
        #print(colWidhts)
        #print(len(colWidhts))
    for k in range(len(colWidhts)):
        for v in range(len(colWidhts)):
            print(table[k][v].rjust(colWidhts[k]), end='')
            

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

    
    
