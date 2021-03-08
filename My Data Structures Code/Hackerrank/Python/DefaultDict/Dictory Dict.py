# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?h_r=next-challenge&h_v=zen&isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Sample input
5 3
a
a
b
a
b
a
b
c
Sample Output
1 2 4
3 5
-1
'''

n, m = input().split()
n = int(n)
m = int(m)
# print(n)
# print(m)
toCheck = []
toCheckFrom = []
for i in range(n):
    val = input()
    toCheck.append(val)

for i in range(m):
    val = input()
    toCheckFrom.append(val)
    
# print(toCheck)
# print(toCheckFrom)
mydict = []
myAllDict = []
tempIndex = []
counter = 0

def finding(Nemo, Sea):
    counter = 0
    temp = []
    for i in range(len(Sea)):
        if(Sea[i] == Nemo):
            new = i+1
            temp.append(new)
            counter +=1
    if(counter ==0):
        return False
    else:
        return temp

for i in range(len(toCheckFrom)):
    mydict = []
    tempIndex = []
    # counter = 0
    # for j in range(len(toCheck)):
    #     if(toCheckFrom[i] in toCheck[j]):
    #         # print("to check from is ",toCheckFrom[i],'and other is ',toCheck[j])
    #         tempIndex.append(j+1)
    #         counter +=1
    indexes = finding(toCheckFrom[i],toCheck)
        # else:
            # tempIndex.append(-1)            
            # print("ITS NOT to check from is ",toCheckFrom[i],'and other is ',toCheck[j])            
    # print("*****************************************************COUNTER*****************************************************",counter)
    if(indexes == False):
        tempIndex.append(-1)
        mydict = [toCheckFrom[i], tempIndex]
    elif(indexes != False):    
        mydict = [toCheckFrom[i],indexes]
    myAllDict.append(mydict)
    
# print(myAllDict)
for i in range(len(myAllDict)):
    for j in range(len(myAllDict[i][1])):
        print(myAllDict[i][1][j], end=" ")
    print("")
# print(myAllDict)