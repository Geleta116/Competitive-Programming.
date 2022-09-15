class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = -1
        out = 0
        
        while i<=len(people)+j:
            if people[i]+people[j]>limit:
                out+=1
                j-=1
            else:
                i+=1
                j-=1
                out+=1
        return out
