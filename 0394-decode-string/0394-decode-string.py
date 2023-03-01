class Solution:
    def decodeString(self, s: str) -> str:
        
        lastindex = [0]
        integer = ""
        
        def decoder(start,integer,lastindex):
            if start >= len(s):
                return ""
            elif s[start] == "]":
                lastindex[0] = start
                return ""
            elif s[start] == "[":
                return int(integer) * decoder(start+1,"",lastindex) + decoder(lastindex[0]+1, "", lastindex)
            elif s[start].isnumeric():
                
                return decoder(start + 1, integer + s[start], lastindex)
            else:
                return s[start] + decoder(start+1,integer,lastindex)
        return decoder(0,"",lastindex) 
        
      