class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        #initialize an array with -1
        next_greater_list = [-1 for index in range(len(nums))]
        
        #create a dictionary to store indices and values
        #create a monotonic stack
        stack = []
        container = defaultdict(lambda : 0)
        
        #get the original length of the array
        #concatinate the array for circular purpose
        #exclude the last element
        len_nums = len(nums)
        nums = nums + list(nums[:-1])
        
        
        #iterate and fill the stack appropriately
        for index,num in enumerate(nums):
            
            if not stack:
                stack.append([num , index])
            else:
                if stack[-1][0] >= num:
                    stack.append([num , index])
                else:
                    while stack and stack[-1][0] < num:
                        integer, ind = stack.pop()
                        container[ind] = num
                    stack.append([num , index])
        
        #populate the output array with the new founf index and numbers
        for keys in container:
            if keys < len_nums :
                next_greater_list[keys] = container[keys]
                
        #return the output
        return next_greater_list
                
        
            
       