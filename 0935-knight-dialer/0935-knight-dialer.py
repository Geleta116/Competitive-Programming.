class Solution:
    def knightDialer(self, n: int) -> int:
        
        graph = {0: [4,6], 1:[6,8], 2 :[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8 :[1,3], 9:[2,4]}
      
        
        @cache
        def dp(num, curr):
            
            if num == 0:  
                return 1
            
            ans = 0
            for child in graph[curr]:
                ans  += dp(num-1, child) 
            return ans
        
        
        out = 0     
        for idx in range(10):
            out += dp(n-1,idx)  
            
        return out % (10 ** 9 + 7)
            
        
        
        