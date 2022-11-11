class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1]*len(nums1)
        for indi,item in enumerate(nums1):
            ind_item = nums2.index(item)
            l2 = nums2[ind_item::]
            len_l2 = len(l2)
            a = 0
            print(l2)
            while a < len_l2:
                if l2[a]>item:
                    out[indi]=l2[a]
                    break
                else:
                    a+=1
                    
                
        return out
            
        