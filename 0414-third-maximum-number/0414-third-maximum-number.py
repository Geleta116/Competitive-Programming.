class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        else:
           
            temp=sorted(nums,reverse=True)
            d = Counter(temp)
            keys = list(d.keys())
            sorted(keys,reverse = True)
            if len(keys)<3:
                return max(keys)
            else:
                return keys[2]
            
           

