from collections import Counter

class Solution :
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        result = []
        if len(changed)%2!= 0:
            return result
        else:
            count = Counter(changed)
            changed.sort()
            for num in changed:
                if num != 0 and count[num]>0 and count[num*2]>0:
                    count[num]-=1
                    count[num*2]-= 1
                    result.append(num)
                elif num == 0 and count[num]>=2:
                    count[num]-=2
                    result.append(num)


            if len(result)==len(changed)//2:
                return(result)
            else:
                return([])

