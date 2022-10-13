class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)==0 or len(nums2)==0:
            return []
        if len(nums1)<=len(nums2):
            out = []
            nums1.sort()
            i = 0 
            o = []
            while i<len(nums1):
                j = 0
                while j<len(nums2):
                    if nums1[i]==nums2[j] and j not in o:
                            out.append(nums1[i])
                            o.append(j)
                            break
                        
                    j+=1
                i+=1
            return out
        else:
            nums2.sort()
            out = []
            i = 0 
            o = []
            while i<len(nums2):
                j = 0
                while j<len(nums1):
                    if nums2[i]==nums1[j]  and j not in o:
                        out.append(nums2[i])
                        o.append(j)
                        break
                    j+=1
                i+=1
            return out
        