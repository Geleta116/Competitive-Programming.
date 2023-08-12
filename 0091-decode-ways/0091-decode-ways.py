class Solution:
    def numDecodings(self, s: str) -> int:
        groups = set()
        for num in range(1, 27):
            groups.add(str(num))  
        memo = defaultdict(int)
            
        def checker(index):
            if index in memo:
                return memo[index]
            
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            
            ones = checker(index + 1)
            twos = 0
            if index < len(s) - 1 and s[index:index + 2] in groups:
                twos = checker(index + 2)
            memo[index] = ones + twos
            return ones + twos
        
        return checker(0)
