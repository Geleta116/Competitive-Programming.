class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        greatest = max(nums)
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
            
        return gcd(smallest, greatest)
        
        