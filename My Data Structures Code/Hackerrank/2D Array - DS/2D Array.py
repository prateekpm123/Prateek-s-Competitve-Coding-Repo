# https://www.hackerrank.com/challenges/2d-array/problem

array = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
rowEnd = len(array)
columnEnd = len(array[0])
row = 0
column = 0
allSets = []
while(row !=rowEnd-2):
    # print("row is ", row)
    column =0
    while(column != columnEnd-2):
        # print("column is ", column)
        firstRow = [row , column + 3]
        secondRow = [row + 1, column+1]
        thirdRow = [row + 2, column + 3]
        sets = []
        for i in range(firstRow[1]-3, firstRow[1],1):
            # print(i)
            sets.append(array[firstRow[0]][i])
        sets.append(array[secondRow[0]][secondRow[1]])
        for i in range(thirdRow[1]-3, thirdRow[1],1):
            sets.append(array[thirdRow[0]][i])
        # print("Row is ", row, column)
        # print(sets)
        allSets.append(sets)
        column = column+1
    row = row +1
# print(allSets)
allSum = []
for i in range(len(allSets)):
    sums = 0
    for j in range(7):
        sums += allSets[i][j]
    allSum.append(sums)

allSum.sort()
print(allSum[len(allSum)-1])
