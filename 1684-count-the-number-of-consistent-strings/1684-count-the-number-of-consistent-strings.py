class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            wor  = set(word)
            for a in wor:
                if a not in allowed:
                    break
            else:
                count +=1
        return count
                
        
        