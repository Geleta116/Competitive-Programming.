class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        if len(s1) == len(s2):
            if Counter(s1)==Counter(s2):
                return True
        count_s1 = dict(Counter(s1))
        
        count_s2 = defaultdict(int)
        
        start = 0
        for end in range(len(s2)):
            if count_s1 == count_s2:
                    return True
            
            if end-start<len(s1):
                count_s2[s2[end]]+=1
            else:
                count_s2[s2[end]]+=1
                count_s2[s2[start]]-=1
                if count_s2[s2[start]]==0:
                    count_s2.pop(s2[start])
                start += 1

                if count_s1 == count_s2:
                    return True
        return False
        
        