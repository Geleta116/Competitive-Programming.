class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []
        
    def push(self, val: int) -> None:
        self.stack3.append(val)
        
        while self.stack1 and self.stack1[-1] < val:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(val)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
            
        
        
        
            
        
    def pop(self) -> None:
        if self.stack3:
            popped = self.stack3.pop()
            if self.stack1 and popped == self.stack1[-1]:
                self.stack1.pop()
            while self.stack1 and self.stack1[-1] not in self.stack3:
                self.stack1.pop()
                
            
        
            
    
    def isEmpty(self):
        if self.stack3:
            return False
        return True
       
        

    def top(self) -> int:
        if self.stack3:
            return self.stack3[-1]
        
        

    def getMin(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        return 0
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
