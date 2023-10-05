class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        checkerLeng = len(nums)//3
        if checkerLeng == 0:
            return list(set(nums))
        
        output = []
        temp = 1
        
        for idx in range(1, len(nums)):
           
            if nums[idx] == nums[idx - 1]:
                temp += 1
            else:
                temp = 1
                
            if temp > checkerLeng:
                if output and output[-1] != nums[idx]:
                    output.append(nums[idx])
                elif not output:
                    output.append(nums[idx])
            
        return list(output)
    
    
    
    