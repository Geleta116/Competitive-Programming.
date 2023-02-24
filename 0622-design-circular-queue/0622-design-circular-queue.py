class ListNode:
    
    def __init__(self,val=0, next = None):
        self.val = val
        self.next = next
        

class MyCircularQueue:

    def __init__(self, k: int):
        new = ListNode()
        self.head = new
        self.tail = new
        self.size = 0
        self.k = k

              

    def enQueue(self, value: int) -> bool:
        if self.size == 0:
            newnode = ListNode(value)
            self.head = newnode
            self.tail = newnode
            
            self.size += 1
            return True
        elif self.size < self.k:
            newnode = ListNode(value)
            self.tail.next = newnode
            self.tail = newnode
            self.size += 1
            return True
        else:
            return False
        
        

    def deQueue(self) -> bool:
        if self.size>0:
            temp = self.head 
            self.head = self.head.next
            temp.next = None
            self.size -=1
            return True
        else:
            return False
        
        

    def Front(self) -> int:
        if self.size > 0 and self.head:
            return self.head.val
        else:
            return -1
        
        
    def Rear(self) -> int:
        if self.size > 0 and self.tail:
            return self.tail.val
        else:
            return -1
       

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()






#this is the circular linked list implementation

# class ListNode:
    
#     def __init__(self,val=None, next = None):
#         self.val = val
#         self.next = next
        

# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.head = ListNode()
#         self.tail = self.head
#         while k > 0:
#             newnode = ListNode()
#             self.tail.next = newnode
#             self.tail = newnode
#             k -= 1
#         self.tail.next = self.head
#         self.tail = self.head
        
              

#     def enQueue(self, value: int) -> bool:
#         if self.tail == None:
#             self.tail.val = value
#             self.tail = self.tail.next
#             return True
#         return False`
        
        

#     def deQueue(self) -> bool:
#         if self.head == None:
#             return False
#         else:
#             self.head.val = None
#             self.head = self.head.next
#             return True
#         return False
        

#     def Front(self) -> int:
#         if self.head:
#             return self.head.val
#         return -1
        

#     def Rear(self) -> int:
#         if self.tail:
#             return self.tail.val
#         return -1
        

#     def isEmpty(self) -> bool:
#         if self.head:
#             return False
#         return True
        

#     def isFull(self) -> bool:
#         if self.tail.next != None:
#             return True
#         return False
        


# # Your MyCircularQueue object will be instantiated and called as such:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()