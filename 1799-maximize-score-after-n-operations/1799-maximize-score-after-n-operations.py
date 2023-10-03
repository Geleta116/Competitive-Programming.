class Solution:
    def maxScore(self, nums: List[int]) -> int:
        self.dp = defaultdict(int)
        nums.sort()
        
        def backtrack(arr, time):
            if not arr:
                return 0
            
            arr.sort()
            if tuple(arr) in self.dp:
                return self.dp[tuple(arr)]
            
            maxi = 0
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    temp = arr[:]
                    ith = temp.pop(i)
                    jth =  temp.pop(j - 1)
                    maxi = max (time * math.gcd(ith,jth) + backtrack(temp, time + 1),  maxi)
                                
            self.dp[tuple(arr)] = maxi         
            return maxi
        
        return backtrack(nums,1)
                    
        