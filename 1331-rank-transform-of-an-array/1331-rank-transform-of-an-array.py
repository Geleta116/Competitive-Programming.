class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x = arr
        print(arr)
        print(x)
        x = list(set(x))
        x.sort()
        print(x)
        l = {}
        for j,n in enumerate(x):
            l[n]=j+1
            
        for i in range(len(arr)):
            arr[i]= l[arr[i]]
                    
        return arr
        
                
            
        