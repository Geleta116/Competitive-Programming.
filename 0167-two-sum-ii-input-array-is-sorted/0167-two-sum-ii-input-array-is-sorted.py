class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            tar = target-n
            if tar in d:
                return [d[tar],i+1]
            d[n] = i+1
        
        