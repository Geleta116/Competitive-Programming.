class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.list = []
        self.notequalindex = -1
        
        

    def consec(self, num: int) -> bool:
        self.list.append(num)
        if (num != self.value):
            self.notequalindex = len(self.list)-1
        
        if len(self.list)<self.k:
            return False
        else:
            return (len(self.list)-1)-self.notequalindex >= self.k
            # if self.notequal  in self.list[len(self.list)-self.k:]:
            #     return False
            # else:
            #     return True
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)