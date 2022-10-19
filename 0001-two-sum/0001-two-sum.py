class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i,n in enumerate(nums):
            temp = target - n
            if temp in check:
                return [check[temp],i]
            check[n] =  i
            
                    
        