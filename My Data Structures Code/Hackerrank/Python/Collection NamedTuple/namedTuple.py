# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
'''
INPUT TESTCASE 1
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   


INPUT TESTCASE 2
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Sample Output

TESTCASE 01
78.00

TESTCASE 02
81.00
'''



# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
num = int(input())

heading = input().split() 
Report = namedtuple('Report',[heading[0], heading[1], heading[2], heading[3]])
marks = []
# print(Report)
# lists.append(Report(3,'Marks', 'Name', 'Class'))
# print(lists)
for i in range(num):
    tempMarks = input().split()
    temp = Report(tempMarks[0],tempMarks[1],tempMarks[2],tempMarks[3])
    # print(temp.NAME)
    marks.append(temp)


allmarks = []
# print('asdf ' ,marks[1].NAME)
for i in range(num):
    temp1 = marks[i].MARKS
    allmarks.append(temp1)
    
allmarks = list(map(int, allmarks))
# print(allmarks)
total = 0
for i in range(num):
    total += allmarks[i]
    
# print(total)
avg = total/num
print(avg)
    
    
# print(marks)
