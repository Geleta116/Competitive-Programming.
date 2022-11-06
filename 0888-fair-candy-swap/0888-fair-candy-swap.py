class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_x = sum(aliceSizes)
        sum_y = sum(bobSizes)
        dif = (sum_x - sum_y)//2
        for item in range(len(bobSizes)):
            bobSizes[item] += dif
        temp = []
        print(bobSizes)
        for new_items in aliceSizes:
            if new_items in bobSizes:
                return [new_items,new_items-dif]
        
        
        