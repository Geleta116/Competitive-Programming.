class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        nums = []
        self.pairs = 0
        for index in range(len(nums1)):
            
            nums.append(nums1[index] - nums2[index])
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)


        
        def merge(left, right):
            arr = []
            indexleft = 0
            indexright = 0
            
            for item in left:
                
                start = bisect_left(right,item - diff)
                self.pairs += len(right) - start
                
            while indexleft < len(left) and indexright < len(right):
                
                if left[indexleft] <= right[indexright]:
                    
                    arr.append(left[indexleft])
                    indexleft += 1
                    
                else:
                    
                    arr.append(right[indexright])
                    indexright += 1
                    
            while indexleft < len(left):
                
                arr.append(left[indexleft])
                indexleft += 1

            while indexright < len(right):
                
                arr.append(right[indexright])
                indexright += 1

            return arr
        
        mergeSort(0, len(nums) - 1, nums)
        
        return self.pairs
        
        
        
        
        
        
        
        
            
            