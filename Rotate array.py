class Solution:
   
    def rotate(self, nums: List[int], k: int) -> None:
            self.k = k%len(nums)
            def reverse(start, last):
                 while start<last:
                        nums[start],nums[last]=nums[last],nums[start]
                        start+=1
                        last-=1
            reverse(0,len(nums)-1)
            reverse(0,self.k-1)
            reverse(self.k,len(nums)-1)
        
            
            """
            Do not return anything, modify nums in-place instead.
            """
