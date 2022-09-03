class MinStack:

    def __init__(self):
        self.stack = []
        self.topp = -1
        self.min = None
        self.mini=[]
        
    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.min=val
            self.mini.append(self.min)
            self.stack.append(val)
            self.topp+=1
        else:
            if self.min>val:
                self.min=val
                self.mini.append(self.min)
                self.stack.append(val)
                self.topp+=1
            elif self.min<val:
                self.stack.append(val)
                self.topp+=1
            elif self.min==val:
                self.stack.append(val)
                self.topp+=1
                self.mini.append(self.min)
                
            
        
    def pop(self) -> None:
        if (self.isEmpty()):
            self.min = None
            self.mini=[]
            return "is Empty"
        else:
            self.topp -=1
            x =self.stack.pop()
            if self.mini[-1]==x:
                if len(self.mini)!=0:
                    self.mini.pop()
                    if len(self.mini)==0:
                        self.min = None
                    else:
                        self.min=self.mini[-1]
            
    
    def isEmpty(self):
        if self.topp==-1:
            return True
        return False
        

    def top(self) -> int:
        if (self.isEmpty()):
            return None
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
