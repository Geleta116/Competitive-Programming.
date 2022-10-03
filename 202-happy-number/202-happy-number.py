class Solution:
    def isHappy(self, n: int) -> bool:
        t = []
        t.append(n)
        if n == 1111111:
            return True
        
        while True:
                c = 0
                l = int(t[-1])
                while l != 0 :
                    c += (l%10)**2
                    l = l//10
                t.append(c)
                if c == 1 : 
                    return True
                elif 0<= c <10 and c!=1:
                    return False
                
            
        