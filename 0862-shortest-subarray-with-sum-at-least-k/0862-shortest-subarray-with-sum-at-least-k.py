class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #create a queue and also a running sum variable
        #make sure that the running sum is always increasing and stored also in your queue
        #along with the index
        if len(nums) == 1:
            if nums[0] >= k:
                return 1
            else:
                return -1
        checker = deque()
        running_sum = 0
        output = float("inf")
        for index,num in enumerate(nums):
            running_sum += num
            # print(checker)
            if running_sum >= k:
                    output = min(output,index+1)
            
            
            while checker and running_sum -  checker[0][0] >= k:
                current = checker.popleft()
                output = min(output, index - current[1])
            
            

            while checker and checker[-1][0] >= running_sum:
                checker.pop()
            checker.append([running_sum, index])
        
        
        
            
        if output == float("inf"):
            return -1
        return output
                
                
                
        
       
    """
       [84,-37,32,40,95]
        167
       """ 
        