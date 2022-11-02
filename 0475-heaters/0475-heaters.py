class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters.append(float(inf))
        l = 0 
        rad = 0
        for i in houses:
            while abs(i-heaters[l+1])<=abs(i-heaters[l]):
                l+=1
            rad = max(rad,abs(i-heaters[l]))
        return rad            