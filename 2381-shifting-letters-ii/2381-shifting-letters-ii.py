class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*len(s)
        for each_shift in shifts:
            start,end,direction = tuple(each_shift)
            if direction > 0 :
                prefix[start] += 1
                if end+1 <len(s):
                    prefix[end + 1] -=1
            elif direction == 0 :
                prefix[start] -= 1
                if end+1 <len(s):
                    prefix[end + 1] +=1
           
            
        
        
        for pre in range(1,len(prefix)):
            prefix[pre] = prefix[pre-1] + prefix[pre]
                
            
        
            
        out = ""
        for index in range(len(prefix)):
            prefix[index] = prefix[index]%26
            if prefix[index] + ord(s[index]) > 122:
                out += chr(96 +prefix[index] + ord(s[index]) - 122)
            else:
                out += chr(prefix[index] + ord(s[index]))
            
        
        return out
                    
                

            
        