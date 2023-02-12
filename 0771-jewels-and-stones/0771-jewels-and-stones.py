class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ct = Counter(jewels)
        ct2 = Counter(stones)
        out = 0
        for i in ct:
            if i in ct2:
                out+= ct2[i]
        return out