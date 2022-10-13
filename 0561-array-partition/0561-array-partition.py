class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        case = 0
        i = 0
        while i<len(nums):
                case+=nums[i]
                i+=2
           
            
        return case
        