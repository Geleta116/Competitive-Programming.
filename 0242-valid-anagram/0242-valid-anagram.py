class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct = Counter(s)
        dt = Counter(t)
        return ct==dt
    
            
        
        