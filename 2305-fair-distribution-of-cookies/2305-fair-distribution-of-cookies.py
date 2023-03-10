class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        self.out = float("inf")
        cookies.sort(reverse = True)
        
        def backtrack(i,bucket):
            
            if i == len(cookies) :
                self.out = min(self.out, max(bucket))
                return
            
            if max(bucket) >= self.out:
                return
            
            for index in range(len(bucket)):
                bucket[index] += cookies[i]
                backtrack(i + 1,bucket)
                bucket[index] -= cookies[i]
               
                
        backtrack(0,[0 for leng in range(k)])
        
        return self.out

        