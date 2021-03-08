class TreeNode:
    def __init__(self):
        self.data = None
        self.children = []
        self.parent = None
        self.size = 0

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
        self.size += 1

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level



    def printTree(self):
        space1 = " " * self.getLevel() * 3
        # print(self.getLevel())
        print(space1, self.data, " -> ")
        
        # if self.children:
        #     count = 0
        #     for child in self.children:
        #         space = " " * self.children[count].getLevel() * 2
        #         print(space, child.data, "," ,end="")
        #         count += 1
        #     print(".")

        if self.children:
            for child in self.children:
                child.printTree()

# class StackNode:
#     def __init__(self, data):
#         self.elements = []
#         # self.size

#     def appendStackNode(self, data):
#         element = TreeNode()
#         element.data = data
#         # self.elements

def peek(stack):
    if(len(stack) == 0):
        return None
    else:
        length = len(stack)
        return stack[length -1]

def sizeOfTree(root):
    total = 0
    for child in root.children:
        val = sizeOfTree(child)
        total = total + val

    total += 1
    return total

# This will take an input of an array and will return a tree
# In making the tree the major part is about, when to add the child, stack is just helping us ! and if conditions determine which node
    # is going to get added where
def MakeTree(array):
    root = TreeNode()

    stack = []
    for i in range(len(array)):
        if (array[i] == -1):
            stack.pop()
        else:
            t = TreeNode()
            t.data = array[i]
            # t.addChild(array[i])

            if (len(stack) > 0):
                val = peek(stack)
                val.addChild(t)
            else:
                root = t

            stack.append(t)
    return root
 
def maxInTree(tree):
    maxi = -9999999999999999999
    # totalmax = -99999999999999999
    for child in tree.children:
        # if(child.data == None):
        #     return maxi
        childMax = maxInTree(child)
        # print("childmax is ", childMax)
        maxi = max(childMax, maxi)
        # print("maxi is ", maxi)

    # print("tree data is ",tree.data)
    maxi = max(tree.data, maxi)
    # maxi = totalmax
    return maxi
    # print(totalmax)

def heightOfATree(tree):
    height = -1                     # IF height is asked in terms of edges then, height= -1 : IF asked in terms of nodes then, height = 0
    for child in tree.children:
        childheight = heightOfATree(child)
        height = max(height,childheight )
    height += 1
    return height

def traversal(tree):
    # if (tree.children == None):
    #     return
    print("Node Pre", tree.data)
    for child in tree.children:
        print("Edge Pre", str(tree.data)+ "--"+str(child.data))
        traversal(child)
        print("Edge Post", str(tree.data)+ "--"+str(child.data))

def insert(queue,val):
    queue.append(val)
    return queue

def removeFromQueue(queue):
    val = queue.pop(0)
    return(queue, val)

def levelOrderTraversal(tree):

    # ****************** MY CODE ********************
    if (root == None):
        return;
   
    # Standard level order traversal code
    # using queue
    q = []  # Create a queue
    q.append(root); # Enqueue root 
    while (len(q) != 0):
     
        n = len(q);
  
        # If this node has children
        while (n > 0):
         
            # Dequeue an item from queue and print it
            p = q[0]
            q.pop(0);
            print(p.data, end=' ')
   
            # Enqueue all children of the dequeued item
            for i in range(len(p.children)):
             
                q.append(p.children[i]);
            n -= 1
   
        # print() # Print new line between two levels
    # queue = []
    # queue.append(tree.data)
    # print(queue[0])
    # while(len(queue)!=0):
    #     queue,val = removeFromQueue(queue)
    #     print(val)
    #     # len(queue)
    #     print(len(tree.children))
    #     # print(queue)
    #     for child in tree.children:
    #         queue.append(child.data)


def levelOrderTraversalZigZag(tree):
    # tree.printTree()
    ms = []
    cs = []
    ms = [tree]
    # print(ms[0].data)
    # test = ms.pop()
    # print(test.children)
    # print(ms)
    level = 0
    while(len(ms) > 0):
        test = ms.pop()
        print(test.data, end=" ")

        if(level % 2 == 0):
            for i in test.children:
                cs.append(i)
                # print(cs)
        else:
            for i in range(len(test.children)-1,-1,-1):
                child = test.children[i]
                cs.append(child)
        

        if(len(ms)==0):
            ms = cs
            cs = []
            level += 1
            print()


if __name__ == '__main__':
    array = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
    # array = [10, 20, -1, 30, 50, -1, 60, -1, -1, 40, -1, -1]
    # array = []
    # num = int(input())
    # array = []
    # array = list(map(int, input().split()))
    # num = int(input())
    # for i in range(num):
    #     val = int(input())
    #     array.append(val)

    root = MakeTree(array)
    levelOrderTraversalZigZag(root)
    root.printTree()
    # traversal(root)
    # print(heightOfATree(root))
    # print(root.getLevel())
    # print(maxInTree(root))