class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.maxi = 0
        
        def backtrack(index,lis):
            if len("".join(lis)) == len(set("".join(lis))):
                self.maxi = max(self.maxi, len("".join(lis)))
            
            if index >= len(arr):
                return
            
           
            
            lis.append(arr[index])
            backtrack(index + 1, lis)
            lis.pop()
            backtrack(index + 1, lis)
            
            
            
            
            
        backtrack(0,[])
        return self.maxi
            
            
            
            
        