class Solution:
    def splitString(self, s: str) -> bool:
        
        self.arr = []
        def split(arr,start):
            if start >= len(s):
                return len(arr) > 1
            
            for end in range(start,len(s)):
                val = int(s[start:end+1])     
                if not arr or arr[-1] - val == 1:
                    arr.append(val)
                    if split(arr,end + 1):
                        return True   
                    arr.pop()
                    
            return False
        
        return split(self.arr, 0)
                    
                
                
            
            
       
