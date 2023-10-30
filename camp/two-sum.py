class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = defaultdict(int)
        for idx,item in enumerate(nums):
            if target - item in store:
                return [idx, store[target - item]]
            store[item] = idx
        return []