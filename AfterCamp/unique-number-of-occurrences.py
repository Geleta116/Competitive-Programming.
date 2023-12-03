class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        arr.append(1001)
        count = set()
        
        left = 0
        right = 1
        curr = 1
        
        while right < len(arr):
            if arr[right] == arr[left]:
                curr += 1
                right += 1
            else:
                if curr in count:
                    return False
                count.add(curr)
                curr = 1
                left = right
                right += 1
                
                
        return True
            