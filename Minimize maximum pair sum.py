class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = -1
        length = len(nums)
        n = []
        while length+j>i:
            n.append([nums[i],nums[j]])
            i+=1
            j-=1
        l = []
        for i in n:
            summ = 0
            summ = i[0]+i[1]
            l.append(summ)
        return max(l)
        
