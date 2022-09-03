class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            x = nums2[j]
            while j<len(nums2):
                if j == len(nums2)-1:
                    ans.append(-1)
                    break

                else:
                    if x<nums2[j+1]:
                        ans.append(nums2[j+1])
                        break
                j+=1
        return(ans)

        
