class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        par  = defaultdict(int)
       
        for num in nums:
            par[num] = num
            
        
        def find(x):
            if x != par[x]:   
                par[x] =  find(par[x])
            return par[x]
        
        def union(num1, num2):
            par1, par2 = find(num1), find(num2)
            if par1 >= par2:
                par[par2] = par1
                find(num2)
            
            else:
                par[par1] = par2
                find(num1)
        
        for num in nums:
            if (num + 1 ) in par:
                union(num, num + 1)
        for num in nums:
            find(num)
        
        counter = defaultdict(int)
        for key in par:
            counter[par[key]] += 1
        
        if counter.values():
            return max(counter.values())
        return 0
       
                
                