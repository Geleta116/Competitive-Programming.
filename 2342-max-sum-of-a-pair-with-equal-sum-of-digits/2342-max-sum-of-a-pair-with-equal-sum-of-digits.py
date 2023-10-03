class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        sums = defaultdict(list)
        
        for num in nums:
            a = list(str(num))
            for i in range(len(a)):
                a[i] = int(a[i])
                
            sums[sum(a)].append(num)
        for key in sums:
            sums[key].sort()
        output = -1
        for key in sums:
            if len(sums[key]) >= 2:
                output = max(output, sums[key][-1] + sums[key][-2])
                
        return output