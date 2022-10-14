class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        h = len(nums)-1
        while l <= h:
            cent = (l+h)//2
            count = 0
            count = sum(nu <= cent for nu in nums)
            if count > cent:
                dup = cent
                h = cent-1
            else:
                l = cent+1
                
        return dup
                
        
        