class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k
        
              

    def enQueue(self, value: int) -> bool:
        if self.k != 0:
            self.queue.append(value)
            self.k -= 1
            return True
        return False

        
    def deQueue(self) -> bool:
        if len(self.queue)>0:
            self.queue.popleft()
            self.k += 1
            return True
        return False
        
    
    
    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[0]
        
        

    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[-1]

        
    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

        

    def isFull(self) -> bool:
        if self.k == 0:
            return True
        return False
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



# class ListNode:
    
#     def __init__(self,val=0, next = None):
#         self.val = val
#         self.next = next
        

# class MyCircularQueue:

#     def __init__(self, k: int):
#         new = ListNode()
#         self.head = new
#         self.tail = new
#         self.size = 0
#         self.k = k

              

#     def enQueue(self, value: int) -> bool:
#         if self.size == 0:
#             newnode = ListNode(value)
#             self.head = newnode
#             self.tail = newnode
            
#             self.size += 1
#             return True
#         elif self.size < self.k:
#             newnode = ListNode(value)
#             self.tail.next = newnode
#             self.tail = newnode
#             self.size += 1
#             return True
#         else:
#             return False
        
        

#     def deQueue(self) -> bool:
#         if self.size>0:
#             temp = self.head 
#             self.head = self.head.next
#             temp.next = None
#             self.size -=1
#             return True
#         else:
#             return False
        
        

#     def Front(self) -> int:
#         if self.size > 0 and self.head:
#             return self.head.val
#         else:
#             return -1
        
        
#     def Rear(self) -> int:
#         if self.size > 0 and self.tail:
#             return self.tail.val
#         else:
#             return -1
       

#     def isEmpty(self) -> bool:
#         if self.size == 0:
#             return True
#         return False
        

#     def isFull(self) -> bool:
#         if self.size == self.k:
#             return True
#         else:
#             return False
        
        


# # Your MyCircularQueue object will be instantiated and called as such:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()






#this is the circular linked list implementation

