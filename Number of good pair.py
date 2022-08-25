class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_good_pair = 0
        for i in range(len(nums)):
            j = 0
            while j<len(nums):
                if i<j:
                    if nums[i] == nums[j]:
                        num_good_pair+=1
                j+=1
        return(num_good_pair)
