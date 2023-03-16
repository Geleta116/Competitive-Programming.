class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.out = False
        self.arr = []
        if int(num) == 0 and len(num)>2:
            return True
        def backtrack(arr,start):
            temp = "".join(arr)
            if len(temp)>0:
                if len(str(int(temp))) == len(num):
                    return len(arr) > 2
                else:
                    if len(num) >2 and len(temp) == len(num) and  int(num[0]) + int(num[1]) == int(num[2]):
                        return len(arr)>2
                    
           
            for end in range(start,len(num)):
                val = num[start:end + 1]
                
                if len(arr) < 2 or int(arr[-1]) + int(arr[-2]) == int(val):
               
                    if len(val)>1 and val[0] == "0" :
                            return False
                    else:
                        arr.append(val)
                        if backtrack(arr,end+1):
                            return True
                        arr.pop()
            return False
        return backtrack(self.arr,0)
                        
  