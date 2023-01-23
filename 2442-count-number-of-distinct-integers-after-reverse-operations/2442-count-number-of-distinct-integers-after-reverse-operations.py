class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        n = len(nums)
        for j in range(n):
            store = 0
            case = nums[j]
            while case>0:
                store  = store *10 + case%10
                case = case//10
            nums.append(store)
                
            
       
        return len(set(nums))
    