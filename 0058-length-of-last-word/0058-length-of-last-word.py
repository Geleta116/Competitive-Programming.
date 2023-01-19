class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        c = s.split(" ")
        return len(c[-1])
        