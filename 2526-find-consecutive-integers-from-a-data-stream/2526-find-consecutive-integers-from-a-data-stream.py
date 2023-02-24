class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.nums = []
        self.last = -1
        

    def consec(self, num: int) -> bool:
        
        if len(self.nums) < self.k - 1 :
            self.nums.append(num)
            if num != self.value:
                self.last = len(self.nums) - 1
            return False
        if num != self.value:
            self.nums.append(num)
            self.last = len(self.nums)-1
            return False
        else:
            self.nums.append(num)
            print(self.last,len(self.nums)- self.k)
            if self.last < len(self.nums) - self.k:
                return True
            elif self.last == -1 and self.value == num:
                return True
            return False
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)