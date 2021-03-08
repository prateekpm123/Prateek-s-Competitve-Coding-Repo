class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()       # this is the head of the linked_list
        self.size = 0



    def append(self, data):
        new_node = node(data)
        curr = self.head         # this gives you the starting point of a linked list
        while(curr.next != None):
            curr = curr.next     # " curr.next " this points to the next node in the linked list starting from the head   
        curr.next = new_node     # After completeing the while loop we have reached the end of linked list, and now we are just appending the new node to the last node i.e. curr.next (in short new_node is getting connected to the linked_list here ) Here the address of the new node (which is a node object) is going in the curr node's next variable
        self.size +=1 
        # print('in apend',self.size)

	
    def testfunction(self):
        print("hello world")
	

    def length(self):
        return(self.size)



    # def erase(self,index):
	# 	if index>=self.length() or index<0: # added 'index<0' post-video
	# 		print("ERROR: 'Erase' Index out of range!")
	# 		return 
	# 	cur_idx=0
	# 	cur_node=self.head
	# 	while True:
	# 		last_node=cur_node
	# 		cur_node=cur_node.next
	# 		if cur_idx==index:
	# 			last_node.next=cur_node.next
	# 			return
	# 		cur_idx+=1

    # ERRORS OCCURENCE IN THE FUNCTION
    # If the data is not present in the linked list then, python will give and error
    # "  'NoneType' object has no attribute 'data' "
    def remove(self, data):
        if(data == None):
            print("Please enter and Element to be removed")
        curr = self.head
        while(curr.data != data):
            last_node = curr
            curr = curr.next
            if(curr.data != None and curr.data == data):              # ERROR: This line will give the ERROR mentioned above
                last_node.next = curr.next
                self.size -= 1
                return
            elif(curr.next == None):              # ERROR: This line will give the ERROR mentioned above
            	print("Element was not found")
        # if(curr.next == None):
        #     print("Element not found !")

    def pop(self):
        if( self.size <= 0):
            print("Stack / Linked List is Empty")
        else:
            curr = self.head
            last_node = None
            while( curr.next != None):
                last_node = curr
                curr = curr.next
            last_node.next = None
            self.size -=1

    def getLastNode(self):
        if(self.size <=0):
            print("Linked List is Empty")
        else:
            curr = self.head
            while(curr.next != None):
                curr = curr.next
            return curr.data

    def getFirst(self):
        if( self.size <= 0):
            print("Stack/ Linked List is Empty")
        else:
            curr = self.head
            curr = curr.next
            return curr.data

    def removeFirst(self):
        if(self.size <=0):
            print("Stack / Linked List is Empty")
        else:
            curr_first = self.head
            curr = self.head
            # curr = curr.next
            curr = curr.next
            curr_first.next = curr.next
            self.size -=1
            return
        # print('First element is ',curr.data)
    
    def removeIndex(self, index):
        curr = self.head
        last_node = 0
        count = -1
        if(index > self.size):
            print("list index out of range")
        elif (index == self.size):
            self.pop()
        elif(index == 0):
            start_node = curr
            curr = curr.next.next
            start_node.next = curr
            self.size -= 1
        elif(-1 < index <self.size):
            while(count != index):
                last_node = curr
                curr = curr.next
                next_node = curr.next
                count += 1
            print(last_node.data, curr.data, next_node.data)
            last_node.next = next_node
            self.size -= 1
        elif(index < 0):
            print("Enter a valid non -ve index")

    def indexAt(self, index):
        if( index < 0):
            print("The index you have entered is -ve")
        elif( index > self.size-1):
            print("You have exceeded the index elements of your linked list")
        else:
            curr = self.head
            for i in range(index+1):
                if(curr.next == None):
                    break
                curr = curr.next
            # print(curr.data)
            return(curr)

    # def appendFirst(self,data):
    #     curr_start = self.head
    #     print(curr_start.next.data)

    # # Prints out the linked list in traditional Python list format.
    def display(self):
        curr = self.head
        elements = []
        while(curr.next != None):
            curr = curr.next
            temp = curr.data
            elements.append(temp)
        print(elements)

    def insert(self, index, data):
        if(index > self.size):
            print('Given Index ', index, ' is greater than size of the linked list which is ', self.size)
        elif(index == self.size):
            self.append(data)
        elif(index < self.size):
            count = -1
            curr = self.head
            new_node = node()
            new_node.data = data
            while( count != index):
                last_node = curr
                curr = curr.next
                count += 1
            last_node.next = new_node
            new_node.next = curr
            self.size += 1

    def newfuntion():
        print("hellow world")

    def appendFirst(self, data):
        curr = self.head
        new_node = node()
        new_node.data = data
        # curr = curr.next
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node
        self.size +=1


    def reverseLinkedListData(self):
        li = 0
        ri = self.size-1
        while(li<ri):
            left = self.indexAt(li)
            right = self.indexAt(ri)

            temp = left.data
            left.data = right.data
            right.data = temp

            li+=1
            ri-=1
        # self.display()
        return self
        
    # NOT WORKING  POINTER IS NOT WORKING
    def reverseLinkedListPointer(self):
        startNewNode = node()
        startNewNode.data = None
        startNewNode.next = None
        # startNewNode = None
        head = self.head
        curr = self.head
        tail = self.getLastNode()


        while( curr.next != None):
            temp = curr.next
            curr.next = startNewNode
            startNewNode = curr
            curr = temp

        print(tail.data)
        # head = self.head
        temp = self.head
        head = tail
        tail = temp
        return self

# {print(test.length())

    # def length(self):
    #     cur = self.head
    #     total = 0
    #     while(cur.next != None ):
    #         total += 1
    #         cur = cur.next
    #     return(total)

    # def display(self):
    #     elems = []
    #     cur_node = self.head
    #     while( cur_node.next != None):
    #         cur_node = cur_node.next
    #         elems.append(cur_node.data)
    #     print(elems)

    # def addLast(self):

    # # Returns the length (integer) of the linked list.
    # def length(self):
    #     cur = self.head
    #     total = 0
    #     while(cur.next!=None):
    #         total += 1
    #         cur = cur.next
    #     return(total)

    # # Prints out the linked list in traditional Python list format.
    # def display(self):
    #     elems=[]
    #     cur_node=self.head
    #     while cur_node.next!=None:
    #         cur_node=cur_node.next
    #         elems.append(cur_node.data)
    #     print(elems)

    # # Returns the value of the node at 'index'.
    # def get(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Get' Index out of range!")
    # 		return None
    # 	cur_idx=0
    # 	cur_node=self.head
    # 	while True:
    # 		cur_node=cur_node.next
    # 		if cur_idx==index: return cur_node.data
    # 		cur_idx+=1

    # # Deletes the node at index 'index'.
    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
    # 		return
    # 	cur_idx=0
    # 	cur_node=self.head
    # 	while True:
    # 		last_node=cur_node
    # 		cur_node=cur_node.next
    # 		if cur_idx==index:
    # 			last_node.next=cur_node.next
    # 			return
    # 		cur_idx+=1

    # # Allows for bracket operator syntax (i.e. a[0] to return first item).
    # def __getitem__(self,index):
    # 	return self.get(index)


    # #######################################################
    # # Functions added after video tutorial

    # # Inserts a new node at index 'index' containing data 'data'.
    # # Indices begin at 0. If the provided index is greater than or
    # # equal to the length of the linked list the 'data' will be appended.
    # def insert(self,index,data):
    # 	if index>=self.length() or index<0:
    # 		return self.append(data)
    # 	cur_node=self.head
    # 	prior_node=self.head
    # 	cur_idx=0
    # 	while True:
    # 		cur_node=cur_node.next
    # 		if cur_idx==index:
    # 			new_node=node(data)
    # 			prior_node.next=new_node
    # 			new_node.next=cur_node
    # 			return
    # 		prior_node=cur_node
    # 		cur_idx+=1

    # # Inserts the node 'node' at index 'index'. Indices begin at 0.
    # # If the 'index' is greater than or equal to the length of the linked
    # # list the 'node' will be appended.
    # def insert_node(self,index,node):
    # 	if index<0:
    # 		print("ERROR: 'Erase' Index cannot be negative!")
    # 		return
    # 	if index>=self.length(): # append the node
    # 		cur_node=self.head
    # 		while cur_node.next!=None:
    # 			cur_node=cur_node.next
    # 		cur_node.next=node
    # 		return
    # 	cur_node=self.head
    # 	prior_node=self.head
    # 	cur_idx=0
    # 	while True:
    # 		cur_node=cur_node.next
    # 		if cur_idx==index:
    # 			prior_node.next=node
    # 			return
    # 		prior_node=cur_node
    # 		cur_idx+=1

    # # Sets the data at index 'index' equal to 'data'.
    # # Indices begin at 0. If the 'index' is greater than or equal
    # # to the length of the linked list a warning will be printed
    # # to the user.
    # def set(self,index,data):
    # 	if index>=self.length() or index<0:
    # 		print("ERROR: 'Set' Index out of range!")
    # 		return
    # 	cur_node=self.head
    # 	cur_idx=0
    # 	while True:
    # 		cur_node=cur_node.next
    # 		if cur_idx==index:
    # 			cur_node.data=data
    # 			return
    # 		cur_idx+=1


test = linked_list()
test.appendFirst(134534)
# test.appendFirst(2)
# test.appendFirst(3)
# test.appendFirst(4)
# test.appendFirst(5)
# test.removedFirst()
# test.removedFirst()
# test.appendFirst(23)
# test.appendFirst(34523)
# test.appendFirst(1)
test.display()
# test.insert(8, 777)
print(test.getFirst())
test.removeFirst()
# test.reverseLinkedListPointer()
# test.reverseLinkedListPointer()
test.display()
# test.testfunction()
# test.removeFirst()
# test.remove(4)
