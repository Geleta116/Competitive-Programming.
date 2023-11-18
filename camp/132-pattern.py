class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        decreasing = []
        mini = float("inf")
        
        for num in nums:
            if not decreasing:
                mini = num
                decreasing.append([num, num])
                continue
                
            while decreasing and decreasing[-1][0] <= num:
                temp = decreasing.pop()
                
            if decreasing and num > decreasing[-1][1]:
                return True
            mini = min(mini, num)
            
            decreasing.append([num, mini])
                
        return False
                
            
                              