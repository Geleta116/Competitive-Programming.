class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.out = []
        
        def backtrack(arr, start):
            if start >= len(s) and len(arr) == 4 and 0 <= int(arr[-1]) < 256  and len(str(int(arr[-1]))) == len(arr[-1]) :
               
                valid_ip = ".".join(arr)
                
                self.out.append(valid_ip)
                return
            
            if arr and (len(arr) > 4 or int(arr[-1]) > 255 or int(arr[-1]) < 0 or len(str(int(arr[-1]))) != len(arr[-1])):
                return
                        
            for end in range(start, len(s)):
                arr.append(s[start: end + 1])
                backtrack(arr, end + 1)
                arr.pop()
        
        backtrack([], 0 )
        return self.out
                
        