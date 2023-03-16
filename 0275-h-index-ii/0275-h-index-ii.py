class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        cit = []
        for index,citation in enumerate(citations):
            cit.append([index,citation])
        
        start = -1
        end = len(citations)
     
        def validate(mid):
            if len(citations) - cit[mid][0] <= cit[mid][1]:
                return True
            return False
        
        while end > start + 1:
            mid = start + (end - start)//2
            if validate(mid):
                end = mid
            else:
                start = mid
        
        return len(citations)-end
        
        
        
        
                