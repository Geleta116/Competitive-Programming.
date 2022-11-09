class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
            a = 0
            b = len(nums)-1
            while a<b:
                if nums[a]%2!=0 and nums[b]%2==0:
                    nums[a],nums[b] = nums[b],nums[a]
                    a+=1
                    b-=1
                elif nums[a]%2!=0 and nums[b]%2!=0:
                    b-=1
                elif nums[a]%2==0 and nums[b]%2==0:
                    a+=1
                elif nums[a]%2==0 and nums[b]%2!=0:
                    a+=1
                    b-=1
            return nums
                
        