class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
                out = [0]*len(temperatures)
                st1 = []
                for index,temp in enumerate(temperatures):
                    while st1 and temp > st1[-1][0]:
                        sttemp,stindex = st1.pop()
                        out[stindex]= (index-stindex)
                    st1.append([temp,index])
                return out
            
