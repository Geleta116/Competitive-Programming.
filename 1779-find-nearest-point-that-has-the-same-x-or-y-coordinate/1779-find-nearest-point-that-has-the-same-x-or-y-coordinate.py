class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        out = float(inf)
        def helper(a,b,c,d):
            return abs(c-a) + abs(d-b)
        helper = []
        for item in points:
            ite_0 = item[0]
            ite_1 = item[1]
            if item[0]==x or item[1]==y :
                case  = abs(ite_0-x) + abs(ite_1-y)
            else:
                case = float(inf)
            # store = helper(x,y,ite_0,ite_1)
            helper.append(case)
        print(helper)
#         for item in points:
#             if item[0]==x or item[1]==y :
#                 store = helper(x,y,item[0],item[1])
#                 out = min(out,store)
#                 # store[]
#                 print(out, item[0], item[1])
#         print(helper)
        out = min(helper)
        if out < float(inf):
            return helper.index(out)
        else:
            return -1
        
        