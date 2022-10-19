class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in range(len(asteroids)):
            if len(s)==0:
                s.append(asteroids[i])
            else:
                if s[-1]>0 and asteroids[i]>0:
                    s.append(asteroids[i])
                elif s[-1]<0 and asteroids[i]<0:
                    s.append(asteroids[i])
                elif  s[-1]>0 and asteroids[i]<0:
                    while s and asteroids[i]<0 and s[-1]>0 and abs(asteroids[i])>s[-1]:
                        s.pop()
                    if not s:
                        s.append(asteroids[i])
                    else:
                        if s[-1] == abs(asteroids[i]):
                            s.pop()
                        else:
                            if s[-1]> abs(asteroids[i]):
                                continue
                            else:
                                s.append(asteroids[i])
                            
                            
                elif  s[-1]<0 and asteroids[i]>0:
                    s.append(asteroids[i])
                            
            print(s)
        return s
                        