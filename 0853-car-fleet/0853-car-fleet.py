class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ou = []
        for i in range(len(position)):
            ou.append([position[i],speed[i]])
        ou.sort()
        print(ou)
        
        s = []
        ou.reverse()
        for j in ou:
            d = target - j[0]
            if not s:
                s.append(d/j[1])
            elif s[-1]< d/j[1]:
                s.append(d/j[1])
        return len(s)
                
            
            
            
            
        