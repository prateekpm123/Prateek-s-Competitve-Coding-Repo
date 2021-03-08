stack = []
exp = "[(a + b) + {(c + d) * (e / f)}]+A"
# exp = input()
def peek(stack):
    stackLen = len(stack)
    stackTop = stack[stackLen-1]
    return stackTop

def balancedBrackets(exp):
    for i in range(len(exp)):
        ch = exp[i]
        if(ch =='(' or ch =='{' or ch=='['):
            stack.append(ch)
        elif(ch == ')'):
            # Something here
            if (len(stack) == 0 or peek(stack) != '('):
                print("false");
                return
            else:
                stack.pop();
        elif(ch == '}'):
            # Something here
            if (len(stack) == 0 or peek(stack) != '{'):
                print("false");
                return
            else:
                stack.pop();
        elif(ch == ']'):
            # Something here
            if (len(stack) == 0 or peek(stack) != '['):
                print("false");
                return
            else:
                stack.pop();
    if(len(stack) == 0):
        print("true")
    else:
        print("false")

balancedBrackets(exp)
