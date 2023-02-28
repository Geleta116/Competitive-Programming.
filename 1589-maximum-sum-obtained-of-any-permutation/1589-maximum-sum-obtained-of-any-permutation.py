class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0 for num in range(len(nums))]
        
        #created the structure of the prefix sum
        for query in requests:
            arr[query[0]] += 1
            
            if query[1] + 1 < len(arr):
                arr[query[1]+1] -= 1
                
        
        #computed the prefix sum
        for num in range(1,len(arr)):
            arr[num] += arr[num-1]
            
        #sorted both the prefix sum and the nums array
        nums.sort()
        arr.sort()
        
        #created the output array and then gave it the result
        output = 0
        for iterator in range(len(nums)):
            output += nums[iterator] * arr[iterator]
        
        return output % (10**9 + 7)
        
        
        
                
                
        