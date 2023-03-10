class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [integer for integer in range(1,n+1)]
        combinations = []
        def backtrack(i, temp):
            if len(temp) == k:
                combinations.append(temp[:])
                return
            elif i >= n:
                return
            
            backtrack(i + 1, temp)
            temp.append(nums[i])
            backtrack(i+1, temp)
            temp.pop()
        backtrack(0,[])
        return combinations            
           
                
                
        