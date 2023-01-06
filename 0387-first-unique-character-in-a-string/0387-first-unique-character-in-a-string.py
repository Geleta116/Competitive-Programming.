class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        store = [[l,i] for i,l in enumerate(s) if ct[l]==1]
        store.sort(key = lambda x: x[1])
        if len(store)== 0:
            return -1
        return store[0][1]
        