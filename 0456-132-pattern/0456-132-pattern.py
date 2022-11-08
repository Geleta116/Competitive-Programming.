class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = []
        mini = nums[0]
        for i in range(1,len(nums)):
            while s and s[-1][0]<=nums[i]:
                 s.pop()
            if s and s[-1][1] < nums[i]:
                return True
            
            
            s.append([nums[i],mini])
            mini = min(mini,nums[i]) 
        return False
                

            
        