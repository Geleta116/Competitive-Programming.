class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        store = num-3
        if store%3 != 0 :
            return []
        else:
            case = store//3
            return [case, case+1, case+2]
        