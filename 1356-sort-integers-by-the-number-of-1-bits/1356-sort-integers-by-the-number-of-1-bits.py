class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        out = []
        for item in arr:
            count = 0
            while item:
                curr = item & 1
                if curr:
                    count += 1
                item >>= 1
            out.append(count)
     
        
        newarr = zip(out,arr)
        newarr = list(newarr)
        
        newarr.sort()
      
        output = []
        for left, right in newarr:
            output.append(right)
        return output
                
            