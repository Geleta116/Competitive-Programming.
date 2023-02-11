class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        point1 = 0
        point2 = 0
        while point1<len(nums1) and point2<len(nums2):
            if nums1[point1]>nums2[point2]:
                point2+=1
            elif nums1[point1]<nums2[point2]:
                point1+=1
            else:
                return nums1[point1]
        return -1
            
        