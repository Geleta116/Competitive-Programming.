class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checker = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and stack[-1]<num:
                    checker[stack.pop()] = num
                stack.append(num)
        
        result = []
        for num in nums1:
            result.append(checker[num])
        return result
            
        