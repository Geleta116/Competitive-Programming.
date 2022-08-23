class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]> nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1],nums[j]
        targ = []
        for l in range(len(nums)):
            if nums[l] == target:
                targ.append(l)
        return targ
        
