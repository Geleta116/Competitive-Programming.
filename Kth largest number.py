class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(map(int, nums))
        k = len(nums)-k
        return(str(nums[k]))
       


'''
The other algorithm I tried is this one the only problem with it is the time limit
exceeded error However it has passed about 207 test cases

class Solution:
    def quick(nums):
        length =  len(nums)
        if length <= 1 :
             return nums
        else :
            pivot=nums.pop ( ) 
        items_lower = [ ]
        items_greater = [ ]
        for item in nums :
            if item < pivot :
                items_greater.append ( item )
            else :
                items_lower.append ( item )
        return (Solution.quick( items_lower ) + [pivot] + Solution.quick(items_greater))


    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for u in range(len(nums)):
            nums[u] = int(nums[u])
        s = Solution.quick(nums)
        n =[]
        for b in range(len(s)):
            n.append(str(s[b]))
        return n[k-1]
'''       
       
