class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win_sum = 0
        size = 0
        maxi = float("-inf")
        for i in range(len(nums)):
            win_sum+=nums[i]
            if i-size+1== k:
                maxi = max(maxi,win_sum)
                win_sum-=nums[size]
                size+=1
        return maxi/k
                
            
            
        