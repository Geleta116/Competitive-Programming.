class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ct = Counter(nums)
        if max(ct.values())>1:
            return True
        return False
        