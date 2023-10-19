class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if not word2:
            return len(word1)
        if not word1:
            return len(word2)
        
        if word1 == word2:
            return 0
        
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        
        insert = self.minDistance(word1, word2[1:])
        delete = self.minDistance(word1[1:], word2)
        replace = self.minDistance(word1[1:], word2[1:])
        
        return 1 + min(insert, delete, replace)