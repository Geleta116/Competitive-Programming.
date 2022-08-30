#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        x = arr
        x.sort()
        i = 0
        while i<(len(x)):
               return (x[i])
               i+=1
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            mini = i 
            for j in range(i,(len(arr))):
                        if arr[j]<arr[mini]:
                           mini = j
            arr[i],arr[mini] = arr[mini],arr[i]
        return(arr)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
