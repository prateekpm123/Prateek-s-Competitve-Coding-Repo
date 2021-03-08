from collections import deque

s = "abcabcabcbb"
que = deque()
points = []
que.append(s[0])
count = 0
allsubs = []
for i in range(1,len(s)):
    temp = s[i]
    # print(s[i])
    count = 0
    for j in range(len(que)):
        if(temp == que[j]):
            count += 1
            samevalue = que[j]
    if(count == 0):
        que.append(temp)
    else:
        allsubs.append(que)
        while(s[i] in que):
            que.pop()
print(allsubs)