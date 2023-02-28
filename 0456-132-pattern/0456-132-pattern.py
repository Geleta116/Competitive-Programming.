class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = nums[0]
        for item in range(1,len(nums)):
            while stack and stack[-1][0] <= nums[item]:
                stack.pop()
            if stack and stack[-1][1] < nums[item]:
                return True
            stack.append([nums[item],mini])
            mini = min(mini,nums[item])
        
         
    
                

            
        