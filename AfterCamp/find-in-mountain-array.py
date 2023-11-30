# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        left = 0
        right = mountain_arr.length() - 1
        
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            mid_val = mountain_arr.get(mid)
            front_val = mountain_arr.get(mid + 1)
            
            if mid_val > front_val:
                right = mid
            else:
                left = mid
           
        def Binary_Search(left, right, direction):
            
            while left + 1 < right:
                mid = left + (right - left) // 2

                mid_val = mountain_arr.get(mid)
                if direction == 1:
                    if mid_val == target:
                        return mid

                    if mid_val > target:
                        right = mid
                    else:
                        left = mid
                else:
                    if mid_val == target:
                        return mid

                    if mid_val < target:
                        right = mid

                    else:
                        left = mid
            return -1
        idx = Binary_Search(-1, right + 1, 1)
        if idx != -1:
            return idx
        idx = Binary_Search(right - 1, mountain_arr.length(), -1)  
        if idx != -1:
            return idx           
        return -1
        
        
            
    
    
    