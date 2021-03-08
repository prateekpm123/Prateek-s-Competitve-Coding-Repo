import
i  akjasf as async
self.data = data
self.next = None


class linkedList:
    def __init__(self):
        self.head = node()  # this is the head of the linked_list
        self.size = 0

class linkedList:
    def __init__(self):
        self.head = node()  # this is the head of the linked_list
        self.size = 0
}
    def append(self, data):
        new_node = node(data)
# set relativenumberdd
        curr = self.head  # this gives you the starting point of a linked list
        while (curr.next != None):
            curr = curr.next  # " curr.next " this points to the next node in the linked list starting from the head
        curr.next = new_node  # After completeing the while loop we have reached the end of linked list, and now we are just appending the new node to the last node i.e. curr.next (in short new_node is getting connected to the linked_list here ) Here the address of the new node (which is a node object) is going in the curr node's next variable
        self.size += 1
        # print('in apend',self.size)
        # ERRORS OCCURENCE IN THE FUNCTION

}
    # ERRORS OCCURENCE IN THE FUNCTION
    
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
   # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
   # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
   # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
   # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
   # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

    # def erase(self,index):
    # 	if index>=self.length() or index<0: # added 'index<0' post-video
    # 		print("ERROR: 'Erase' Index out of range!")
   # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION

    def length(self):
        return (self.size)

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
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # ERRORS OCCURENCE IN THE FUNCTION
    # If the data is not present in the linked list then, python will give and error
    # "  'NoneType' object has no attribute 'data' "
    def remove(self, data):
        if (data == None):
            print("Please enter and Element to be removed")
        curr = self.head
        while (curr.data != data):
            last_node = curr
            curr = curr.next
            if (curr.data != None and curr.data == data):  # ERROR: This line will give the ERROR mentioned above
                last_node.next = curr.next
                self.size -= 1
                return
            elif (curr.next == None):  # ERROR: This line will give the ERROR mentioned above
                print("Element was not foun




