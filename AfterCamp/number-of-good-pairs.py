class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        store = defaultdict(int)
        out = 0
        for i in nums:
            if i in store:
                out += store[i]
                store[i] += 1
            else:
                store[i] = 1
        return out
        