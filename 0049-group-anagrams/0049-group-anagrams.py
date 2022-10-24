class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            x = "".join(sorted(i))
            if x not in d:
                d[x] = []
            d[x].append(i)
        return list(d.values())
        
        