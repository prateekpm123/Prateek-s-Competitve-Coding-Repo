######################################################################################
    #    MY SOLUTION PROBABLY GIVES TIME COMPLEXITY ERROR
######################################################################################
    

exp = "{[(a + b) + {(c + d) * (e / f)}]}+A"


# exp = input()
stack = []
brackets = [['(', ')'],['{','}'],['[',']']]
expList = []
for i in exp:
    expList.append(i)

# find the right bracket
def closingBracket(value):
    for i in range(len(brackets)):
        if(value == brackets[i][1]):
            # typebracket = brackets[i][1]
            return i
        
def peek(array):
    length = len(array)
    return array[length-1]

def otherUnwanted(bracketOtherPair):
    otherPairList = []
    for i in range(len(brackets)):
        if(brackets[i][0] != bracketOtherPair):
            otherPairList.append(brackets[i][0])
    return otherPairList


def balancedBrackets(exp):
    for i in exp:
        # print(i)
        noofBracket = closingBracket(i)
        print('no of bracket is ' ,noofBracket)
        if(noofBracket != None):
            if(i == brackets[noofBracket][1]):
                # print(brackets[noofBracket][1])  
                bracketOtherPair = brackets[noofBracket][0]
                otherUnwantedBrackets = otherUnwanted(bracketOtherPair)
                unwantedBracket1 = otherUnwantedBrackets[0]
                unwantedBracket2 = otherUnwantedBrackets[1]
                print("other bracket pair is ", bracketOtherPair)
                stackLens= len(stack)
            
                while(peek(stack) != bracketOtherPair):
                    if(peek(stack) == unwantedBracket1):
                        return("false")
                    if(peek(stack) == unwantedBracket2):
                        return("false")
                    stack.pop()
                stack.pop()
                print("stack after pop is ", stack)
        else:
            stack.append(i)
            print("stack is ",stack)
    stackLen = len(stack)
    if(stackLen == 0):
        return("true")  
    else:
        return("false")


print(balancedBrackets(expList))

