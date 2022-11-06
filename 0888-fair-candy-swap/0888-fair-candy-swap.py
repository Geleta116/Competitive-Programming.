class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_x = sum(aliceSizes)
        sum_y = sum(bobSizes)
        dif = (sum_x - sum_y)//2
        x = set(aliceSizes)
        y = set(bobSizes)
        for i in x:
            if i - dif in y:
                return  [ i,i-dif]
                
        
        