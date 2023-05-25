class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        bucks = defaultdict(int)
        bucks[5] = 0
        bucks[10] = 0
        bucks[20] = 0
        
        for bill in bills:
            if bill == 5:
                bucks[5] += 1
            elif bill == 10:
                if bucks[5] > 0:
                    bucks[5] -= 1
                    bucks[10] += 1
                else:
                    return False
            elif bill == 20:
                if bucks[5] >0 and bucks[10] > 0:
                    bucks[5] -= 1
                    bucks[10] -= 1
                    bucks[20] += 1
                elif bucks[5] >= 3:
                    bucks[5] -= 3
                    bucks[20] += 1
                else:
                    return False
        return True
        