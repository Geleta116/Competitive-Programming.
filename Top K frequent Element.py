class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<=1:
            return nums
        else:
            counter = Counter(nums)
            s = counter.most_common()
            ans = []
            j = 0
            while k>0:
                ans.append(s[j][0])
                j+=1
                k-=1
            return ans
        
