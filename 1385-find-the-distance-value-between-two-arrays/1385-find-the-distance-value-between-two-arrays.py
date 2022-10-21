class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        print(arr1)
        arr2.sort()
        print(arr2)
        out = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])>d:
                    continue
                else:
                    out+=1
                    break
     
        return len(arr1)-out
                
        