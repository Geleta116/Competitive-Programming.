class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if not s1 and not s2 and not s3:
            return True
        
        if not s3 and (len(s1) > 0 or len(s2)>0):
            return False
        
        if not s1 and not s2 and s3:
            return False
        
        left = False
        right = False
        
        if s1 and s1[0] == s3[0]:
            left = self.isInterleave(s1[1:], s2, s3[1:])
        if s2 and s2[0] == s3[0]:
            right = self.isInterleave(s1, s2[1:], s3[1:])
        
        return left or right
        
        
        
        