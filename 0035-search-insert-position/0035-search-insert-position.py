class Solution:
    def searchInsert(self, queue: List[int], name: int) -> int:
            
            left = -1
            right = len(queue)
            def isgreater(mid):
                if mid == len(queue) or  queue[mid] >= name:
                    return True
                return False
            while right > left + 1:
                mid = left + (right - left) // 2

                if isgreater(mid):
                    right = mid

                else:
                    left = mid
            return right
        