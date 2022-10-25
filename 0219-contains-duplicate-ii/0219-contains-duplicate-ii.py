class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ct = set()
        for i in range(len(nums)):
            if len(ct)>=k+1:
                ct.remove(nums[i-k-1])
            if nums[i] in ct:
                return True
            else:
                ct.add(nums[i])
        return False