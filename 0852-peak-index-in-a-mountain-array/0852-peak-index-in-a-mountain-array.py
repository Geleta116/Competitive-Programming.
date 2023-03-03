class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left  = -1
        right = len(arr) 
        
        def decreasing(arr,index):
            if index + 1 < len(arr):
                if arr[index] > arr[index + 1] :
                    return True
            return False
        
        while right > left + 1:
            mid = left + (right - left) // 2
            if decreasing(arr,mid):
                right = mid
            else:
                left = mid
        return right
        
        