class Node:
    val = None
    leftNode = None
    rightNode = None 
    level = 0
    def __init__(self, val, leftNode, rightNode):
        self.val = val
        self.leftNode = leftNode
        self.rightNode = rightNode

class Pair:
    state = None
    def __init__(self, Node, state):
        self.Node = Node
        self.state = state

# ************* CODE FOR STACK ************
def peek(stack):
    top = stack[len(stack)-1]
    return top

def peekNode(stack):
    topNode = stack[len(stack)-1]
    return topNode

# ************ FUNCTIONS ON BINARY TREE **********
def displayBinaryTree(node):
    if(node == None):
        return
    string = ""
    string += "." if(node.leftNode == None) else str(node.leftNode.val)
    string += " <-"+str(node.val)+" ->"
    string += "." if(node.rightNode == None )  else str(node.rightNode.val) 
    print(string)
    # print(node.leftNode.val,"<-",node.val,"->",node.rightNode.val)
    displayBinaryTree(node.leftNode)
    displayBinaryTree(node.rightNode)

def displayNodes(node):
    if(node == None):
        return
    print(node.val)
    displayNodes(node.leftNode)
    displayNodes(node.rightNode)

def makeBinaryTree(array):
    root = Node(array[0], None, None)
    pair = Pair(root, 1)
    stack = []
    stack.append(pair)
    print(stack[0].state)
    i = 0
    while(len(stack)>0):
        stackLen = len(stack)
        # stackPeekNode = stack[stackLen-1].Node
        if(stack[stackLen-1].state == 1):
            i += 1
            if(array[i] != None):
                ln = Node(array[i], None, None)
                topNode = peekNode(stack)
                topNode.Node.leftNode = ln
                tempPair = Pair(ln, 1)
                stack.append(tempPair)
            else:
                topNode = peekNode(stack)
                topNode.Node.leftNode == None
            topNode.state += 1

        elif( stack[stackLen-1].state == 2):
            i += 1 
            if(array[i] != None):
                rn = Node(array[i], None, None)
                topNode = peekNode(stack)
                topNode.Node.rightNode = rn
                #  = Node(array[i], None, None)
                tempPair = Pair(rn, 1)
                stack.append(tempPair)
            else:
                    topNode = peekNode(stack)
                    topNode.Node.leftNode == None
            topNode.state += 1


        else:
            stack.pop()
        # print(stack[len(stack)-1].Node.val)
    return root

if __name__ == '__main__':
    array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]

    root = makeBinaryTree(array)
    displayBinaryTree(root)
    # displayNodes(root)