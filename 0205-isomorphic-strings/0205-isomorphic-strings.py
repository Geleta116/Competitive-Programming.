class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Store_s = []
        for item in s:
            Store_s.append(s.find(item))
        Store_t = []
        for item in t:
            Store_t.append(t.find(item))
        return Store_s == Store_t
    