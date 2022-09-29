class MyCircularDeque:

    def __init__(self, k: int):
        self.tail = 0
        self.head = 0
        self.k = k
        self.list = [None]*k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif not self.isEmpty():
            self.head = (self.head-1)%self.k
            self.list[self.head]=value
            self.size+=1
            return True
        elif self.isEmpty():
            self.list[self.head]= value
            self.size+=1
            return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        elif not self.isEmpty():
            self.size+=1
            self.tail = (self.tail+1)%self.k
            self.list[self.tail] = value
            return True
        elif self.isEmpty():
            self.list[self.tail]= value
            self.size+=1
            return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        else:
            self.list[self.head]= None
            if self.size == 1:
                self.size-=1
                return True
            else:
                self.size-=1
                self.head = (self.head+1)%self.k
                return True
        
        

    def deleteLast(self) -> bool:
        if self.isEmpty():return False
        else:
            self.list[self.tail]=None
            if self.size == 1:
                self.size-=1
                return True
            else:
                self.size-=1
                self.tail = (self.tail-1)%self.k
                return True
        

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        else:
            return self.list[self.head]
        
        

    def getRear(self) -> int:
        if self.isEmpty():return -1
        else:
            return self.list[self.tail]
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
