class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ["a", "b", "c"]
        self.container = []
        self.out = ""
        
        
        def backtrack(arr):
            current = "".join(arr)
            
            if len(arr) > n:
                return
            
            if n>=2 and len(arr) == n and arr[-2] != arr[-1]:
                current = "".join(arr)
                
                self.container.append(current)
                return
            if n ==  1 and len(arr) == n:
                current = "".join(arr)
                
                self.container.append(current)
                return
                
            if len(arr)>=2 and arr[-2] == arr[-1]:
                return
            
            for index in range(len(letters)):
                arr.append(letters[index])
                backtrack(arr)
                arr.pop()
        
        
        for index in range(len(letters)):
            arr = []
            arr.append(letters[index])
            backtrack(arr)
        
        if k <= len(self.container):
                return self.container[k - 1]
        return self.out
            
            