class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        for index,interval in enumerate(intervals):
            interval.append(index)
        new = list(intervals)
        new.sort()   
        temp = defaultdict(lambda:-1)

        for i in range(len(intervals)):
            temp[i] = -1
        def validate(compare,mid):
            if compare <= new[mid][0]:
                return True
            return False
       
        for index,item in enumerate(intervals):
            
            start = -1
            end = len(intervals)
            
            while end > start + 1:
                mid = start + (end - start)//2
                
                if validate(item[1],mid):
                    
                    end = mid
                else:
                    start = mid
        
            if end<len(intervals):
                temp[index] = new[end][-1]
        
        return temp.values()
