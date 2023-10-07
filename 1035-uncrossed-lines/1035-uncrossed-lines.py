class Solution:
   
    def maxUncrossedLines(self, nums11: List[int], nums21: List[int]) -> int:
        
        @cache
        def  maxUncrossedLiness(nums1, nums2):
            n1 = len(nums1)
            n2 = len(nums2)

            if n1 == 0 or n2 == 0:
                return 0
            
            out = 0
            if nums1[0] == nums2[0]:
                out += 1 + maxUncrossedLiness(tuple(nums1[1:]), tuple(nums2[1:]))
                return out

            left = 0
            right = 0
            mid = 0

            # you have three options
            commonFromNums1Index = 0
            while commonFromNums1Index < len(nums1) and nums1[commonFromNums1Index] != nums2[0]:
                commonFromNums1Index += 1

            if commonFromNums1Index < len(nums1):
                # print(commonFromNums1Index)
                left = 1 + maxUncrossedLiness(tuple(nums1[commonFromNums1Index + 1:]), tuple(nums2[1:]))

            commonFromNums2Index = 0
            while commonFromNums2Index < len(nums2) and nums2[commonFromNums2Index] != nums1[0]:
                commonFromNums2Index += 1

            if commonFromNums2Index < len(nums2):
                right = 1 + maxUncrossedLiness(tuple(nums1[1:]), tuple(nums2[commonFromNums2Index + 1:]))

            mid  = maxUncrossedLiness(tuple(nums1[1:]), tuple(nums2[1:]))
            return max(left, right, mid)
        
        return maxUncrossedLiness(tuple(nums11), tuple(nums21))
            
        
            