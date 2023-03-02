class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #create a queue and also a running sum variable
        #make sure that the running sum is always increasing and stored also in your queue
        #along with the index
        
        checker = deque()
        running_sum = 0
        output = float("inf") 
        # Iterate over the num and increment the running sum
        for index,num in enumerate(nums):
            running_sum += num
            # if the running sum is greater or equal to k check if it is greater
            if running_sum >= k:
                    output = min(output,index+1)
            
            # while the running sum is greater than k try to pop from the left
            while checker and running_sum -  checker[0][0] >= k:
                current = checker.popleft()
                output = min(output, index - current[1])
            
            
            # while the dictionaries last is smaller than the running sum pop 
            while checker and checker[-1][0] >= running_sum:
                checker.pop()
            
            #after you have made sure you have made the deque a monotonic deque 
            #insert the last element
            checker.append([running_sum, index])
        
        
        
            
        if output == float("inf"):
            return -1
        return output
                
                
                
        
       
    
        
