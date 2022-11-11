class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1]*len(nums1)
        stack = []
        for indi,item in enumerate(nums1):
            ind_item = nums2.index(item)
            l2 = nums2[ind_item::]
            len_l2 = len(l2)
            a = 0
            print(l2)
            for i in l2:
                if i>item:
                    out[indi]=i
                    break
                
                
        return out
            
        