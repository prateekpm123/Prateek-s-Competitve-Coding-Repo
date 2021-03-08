# STACK PROBLEM, LOGIC EXPLAINED BY SIR

st = []
# string = "(a + b) + ((c + d))"
value = 0

string = input()
def pop(array):
    length = len(array)
    array.pop()
    return array

def push(array, num):
    length = len(array)
    array.append( num)
    return array

def peek(array):
    length = len(array)
    return array[length-1]

def duplicateBrackets(string):
    for i in range(len(string)):
        ch = string[i]
        if(ch == ')'):
            if(peek(st) == '('):
                print("true")
                return
            else:
                while(peek(st) != '('):
                    pop(st)
                pop(st)
        else:
            push(st,ch)
    print("false")

duplicateBrackets(string)

