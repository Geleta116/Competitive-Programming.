class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        self.count = 0
        def merge(nums, start, end ):
            if start == end:
                return [nums[start]]
            mid = start + (end - start) // 2
            rightside = merge(nums, mid + 1, end)   
            leftside = merge(nums, start, mid)
             
                
            first = 0 
            second = 0
            while second < len(leftside) and first < len(rightside):
                if leftside[second] > 2 * rightside[first]:
                    self.count += len(leftside) - second 
                    first += 1
                else:
                    second += 1
            return mergesort(leftside, rightside)
        
        def mergesort(left, right):
            index1 = 0
            index2 = 0
            output = []
            while index1 < len(left) and index2 < len(right):
                
                if left[index1] <= right[index2]:
                    output.append(left[index1])
                    index1 += 1
                else:
                    output.append(right[index2])
                    index2 += 1
            while index1 < len(left):
                output.append(left[index1])
                index1 += 1
                
            while index2 < len(right):
                output.append(right[index2])
                index2 += 1
            return output
        
        merge(nums, 0 , len(nums) - 1)
        
        return self.count
                    
            
        