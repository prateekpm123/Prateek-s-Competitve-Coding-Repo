# string = input()
finalAns = []
string = "abc"

def getSubseq(string):
    # getSubseq(abc) -> [ , c, b, bc]
    if(len(string) == 0):
        bres = []
        bres.append(" ")
        return  bres


    fch = string[0]
    restoch = string[1:len(string)]
    # print(fch)
    # print(restoch)
    ans = []
    ans = getSubseq(restoch)
    for i in range(len(ans)):
        finalAns.append(ans[i])
    
    for i in range(len(ans)):
        ans[i] = fch+ans[i]
        finalAns.append(ans[i])
    
    return finalAns


print(getSubseq(string))