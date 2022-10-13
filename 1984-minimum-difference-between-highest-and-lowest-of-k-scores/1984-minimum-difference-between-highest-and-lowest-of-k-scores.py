class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = []
        i = 0
        j = k-1
        while j<len(nums):
            l.append(nums[j]-nums[i])
            i+=1
            j+=1
        l.sort()
        return l[0]
        