class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        odd = defaultdict(int)
        even = defaultdict(int)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                even[nums[i]] += 1
            else:
                odd[nums[i]] += 1
                
        num_Even = 0
        num_Odd = 0
        
        if len(nums) % 2 != 0:
            num_Even = ((len(nums) - 1) // 2 )+ 1
            num_Odd = (len(nums) - 1) // 2
        else:
            num_Even = ((len(nums)) // 2 ) 
            num_Odd = (len(nums)) // 2
        
        
        sorted_even_items = sorted(even.items(), key=lambda x: x[1], reverse=True)
        top_even_keys = [item[0] for item in sorted_even_items[:2]]
        
        sorted_odd_items = sorted(odd.items(), key=lambda x: x[1], reverse=True)
        top_odd_keys = [item[0] for item in sorted_odd_items[:2]]
        

        if top_even_keys[0] != top_odd_keys[0]:
            return num_Even - even[top_even_keys[0]] +  num_Odd - odd[top_odd_keys[0]]
           
        elif len(top_even_keys) == 1 and len(top_odd_keys) != 1:
            return min(num_Even,  num_Odd - odd[top_odd_keys[1]])
        
        elif len(top_even_keys) != 1 and len(top_odd_keys) == 1:
            return min(num_Even - even[top_even_keys[1]] , num_Odd)
        
        elif len(top_even_keys) == 2 and len(top_odd_keys) == 2: 
            
            return min( num_Even - even[top_even_keys[0]] +  num_Odd - odd[top_odd_keys[1]], num_Even - even[top_even_keys[1]] +  num_Odd - odd[top_odd_keys[0]])
        else:
            return len(nums) // 2
            