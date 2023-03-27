class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        self.count = [ 0 for num in nums]
        array = []
        for index, num in enumerate(nums):
            array.append([num,index])
            
        def mergesort(left, right, arr):
            
            if left == right:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            leftside = mergesort(left, mid,arr)
            rightside = mergesort(mid + 1, right, arr)
            
            return merge(leftside, rightside)
        
        
        def merge(left, right):
            arr = []
            indexleft = 0
            indexright = 0
            
            for item in left:
                
                greaterIndex = bisect_right(right,item)
                
                self.count[item[1]] += greaterIndex 
                
            
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
       
        mergesort(0, len(array) - 1 ,array)
        
        return self.count
 