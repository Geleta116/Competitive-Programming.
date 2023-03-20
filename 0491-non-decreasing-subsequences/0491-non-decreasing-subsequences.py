class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        
        def backtrack(index, lis):
            if len(lis) >= 2 and lis[-2] <= lis[-1]:
                ans[tuple(lis[:])] = 1
            if len(lis) >= 2 and lis[-2] > lis[-1]:
                return
            if index >= len(nums):
                return
            lis.append(nums[index])
            backtrack(index + 1, lis)
            lis.pop()
            backtrack(index + 1, lis)
            
        backtrack(0,[])
        return ans.keys()
            
        
        