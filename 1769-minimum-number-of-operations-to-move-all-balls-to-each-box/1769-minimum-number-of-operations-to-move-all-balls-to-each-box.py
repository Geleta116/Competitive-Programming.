class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        out=[]
        
        for i in range(len(boxes)):
            ct=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    ct+=abs(i-j)
            out.append(ct)
            
        return out
        