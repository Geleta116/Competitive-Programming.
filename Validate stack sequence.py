class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        s=[]
        while j<len(popped) and i<len(pushed):
            if pushed[i]!=popped[j] and len(s)==0:
                s.append(pushed[i])
                i+=1
            elif pushed[i]==popped[j] and len(s)==0 :
                i+=1
                j+=1
            elif len(s)!=0 and s[-1]==popped[j]  :
                s.pop()
                j+=1
            elif pushed[i]!=popped[j] and len(s)!=0:
                s.append(pushed[i])
                i+=1
            elif pushed[i]==popped[j] and len(s)!=0 :
                i+=1
                j+=1
                
            
        while len(s)!=0 :
            if s[-1]==popped[j]:
                s.pop()
                j+=1
            else:
                return False
        if len(s)==0:
            return True
        else:
            return False
