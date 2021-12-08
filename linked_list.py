from node import Node

class SinglyLinkedList():
    def __init__(self):
        self.tail = None
        self.size = 0 

    def append(self,data):
        node=Node(data)

        if(self.tail == None):
            self.tail = node
        else:
            curr = self.tail 
        
            while curr.next:
                curr = curr.next

            curr.next = node
        
        self.size += 1
    
    def size(self):
        return str(self.size)

    def iter(self):
        curr = self.tail

        while curr:
            val = curr.data 
            curr = curr.next
            yield val

    

        