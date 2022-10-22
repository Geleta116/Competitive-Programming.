class Solution:
    def reverseWords(self, s: str) -> str:
        ou = []
        for k in s:
            ou.append(k)
        print(ou)   
        j = len(ou)-1
        i  = 0 ;
        while i<j:
            ou[j],ou[i] = ou[i],ou[j]
            i+=1
            j-=1
        print(ou)  
        h =""
        for d in ou:
            h+=d
            
        
        l = h.split(" ")
        
        a = 0
        b = len(l)-1
        while a<b:
            l[a],l[b]=l[b],l[a]
            a+=1
            b-=1
        out = " ".join(l)
        return out
        