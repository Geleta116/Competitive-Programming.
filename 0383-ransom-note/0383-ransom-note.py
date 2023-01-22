class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ct = Counter(ransomNote)
        ct2 = Counter(magazine)
        for i in ct:
            if ct[i] > ct2[i]:
                return False
        return True