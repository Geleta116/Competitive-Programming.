class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        check = float("-inf")
        s = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<check:
                return True
            else:
                while s and s[-1]<nums[i]:
                    check = s.pop()
                    
                s.append(nums[i])
        return False

            
        