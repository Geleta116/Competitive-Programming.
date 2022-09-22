class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        end = 0
        l = chars
        s = ""
        while end<len(l):
            if end==len(l)-1:
                if l[end]==l[end-1]:
                    s+=l[end]
                    temp = end
                    end+=1
                    if temp-start!=0:
                        s+=str(temp-start+1)
                elif  l[end]!=l[end-1]:
                    s+=l[end]
                    end+=1
                
           

            elif end != len(l)-1:
                if l[end]!=l[end+1]:
                    s+=l[end]
                    if end-start!=0:
                        s+=str(end-start+1)
                    start = end+1
                    end+=1
                elif l[end]==l[end+1]:
                    end+=1
        out = []
        for i in s:
            out.append(i)
        n = len(out)
        chars[:] = out
        return n
        
    
                
