class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0]*len(temperatures)
        
        for i,celcious in enumerate(temperatures):
            if not stack or stack[-1][0] >= celcious:
                stack.append([celcious,i])
            else:
                while stack and stack[-1][0] < celcious:
                    pos, deg = stack.pop()
                    out[deg] = i - deg 
                stack.append([celcious,i])
        return out
        
