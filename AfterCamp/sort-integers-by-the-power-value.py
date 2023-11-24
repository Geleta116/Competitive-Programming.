class Solution:
    @cache
    def power(self, x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + self.power(x // 2)
            else:
                return 1 + self.power(3 * x + 1)
    def getKth(self, lo: int, hi: int, k: int) -> int: 
        store = []
        for num in range(lo, hi + 1):
            curr = self.power(num)
            store.append([curr, num])
        store.sort()
        return store[k - 1][1]
        