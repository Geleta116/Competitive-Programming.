class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        Total_sum = sum(weights) + 1
        max_value = max(weights) - 1
        
        # print(Total_sum,max_value)
        #define a calidating function
        def validate(weights,capacity):
            running_sum = 0
            numof_days = 0
            for i,weight in enumerate(weights):
                
                running_sum += weight
                
                if running_sum < capacity:
                    if i == len(weights) - 1:
                        numof_days += 1
                        
                elif running_sum ==  capacity:
                    running_sum = 0
                    numof_days += 1
                else:
                    running_sum = weight
                    numof_days += 1
                    if i == len(weights) -  1:
                        numof_days += 1
            # return numof_days
            if  numof_days <=days:
                return True
            return False
        
        # return validate(weights,3)
        #we will use binary search to find the weights
        low = max_value
        high = Total_sum
             

        while low + 1 < high:
             
            mid = low + (high - low) // 2
            if validate(weights, mid):
                high = mid
            else:
                low = mid
        return high
                
                    
                    
                   
                